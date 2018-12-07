# -*- coding: utf-8 -*-


import scrapy
from scrapy_splash import SplashRequest
from ..items import BevolItem
import re
import json
import time
import requests
from lxml import etree
from bs4 import BeautifulSoup


class bevolSpider(scrapy.Spider):
    name = "bevol"
    allowed_domains = ["www.bevol.cn"]
    url = 'https://www.bevol.cn/product'

    def start_requests(self):
        pageList = [6, 7, 8, 9, 10, 11, 12, 13, 15, 20, 47, 30, 38]
        for i in pageList:
            yield SplashRequest(url=self.url + '?category=' + str(i), callback=self.parse, args={'wait': 5}, meta={'splash': {
                        'endpoint': 'render.html'}, 'category': str(i)
            })

    def parse(self, response):
        page = response.xpath('/html/body/div[2]/div[3]/div[4]/div/a[4]/text()')[0].extract()
        url = (response.url).split('?')
        category = response.meta['category']
        i = 1
        while i < 260:
            # url[0] + '?v=2.0' + '&' + url[1] + '&p=' + str(i)
            yield SplashRequest(url=url[0] + '?v=2.0' + '&' + url[1] + '&p=' + str(i), callback=self.parse_list, args={'wait': 5},
                                meta={'splash': {'endpoint': 'render.html'}, 'category': category
                                })
            i += 1

    def parse_list(self, response):
        category = response.meta['category']
        list = response.xpath('/html/body/div[2]/div[3]/div[1]/div[3]/ul/a')
        if len(list) > 0:
            item = BevolItem()
            for l in list:
                url = 'https://www.bevol.cn' + l.xpath('@href')[0].extract()
                item['cosmetics_name'] = l.xpath('@title')[0].extract()
                if item['cosmetics_name'].count("'") > 0:
                    item['cosmetics_name'] = item['cosmetics_name'].replace("'", "`")
                item['cosmetics_absolute'] = l.xpath('li/div[2]/p[@class="absolute p4"]/text()')[0].extract()
                item['cosmetics_absolute'] = item['cosmetics_absolute'].strip()
                item['cosmetics_img'] = l.xpath('li/div[1]/img/@src')[0].extract()
                item['cosmetics_id'] = re.compile(r'\/.*?\/(.*)\.(html)').search(l.xpath('@href')[0].extract()).group(1)
                yield SplashRequest(url, callback=self.parse_detail, args={'wait': 24}, meta={'splash': {
                                        'endpoint': 'render.html'}, 'id': item['cosmetics_id'],
                                        'name': item['cosmetics_name'], 'absolute': item['cosmetics_absolute'],
                                        'img': item['cosmetics_img'], 'category': category
                                })
        else:
            pass

    def parse_detail(self, response):
        item = BevolItem()
        item['category'] = response.meta['category']
        item['cosmetics_name'] = (response.meta['name']).strip()
        item['cosmetics_id'] = response.meta['id']
        detail = response.xpath('/html/body/div[2]/div[4]')
        starList = detail.xpath('div[1]/div[2]/div[1]/div[1]/img/@src').extract()
        item['cosmetics_img'] = response.meta['img']
        item['cosmetics_absolute'] = response.meta['absolute']
        item['cosmetics_url'] = response.url
        stars = []
        for star in starList:
            stars.append(star)
        item['cosmetics_star'] = json.dumps(stars, ensure_ascii=False)
        securityList = detail.xpath('div[1]/div[2]/div[1]/div/a/text()').extract()
        securitys = []
        for security in securityList:
            security = ((security.strip()).replace(' ', '')).replace('\n', '')
            security = {"name": security}
            securitys.append(security)
        item['security_said'] = json.dumps(securitys, ensure_ascii=False)
        ingreduentList = detail.xpath('div[1]/div[@class="cosmetics-info-title   chengfenbiao"]/table/tbody/tr')
        if len(ingreduentList) == 0:
            ingreduentList = detail.xpath('div[1]/div[@class="cosmetics-info-title  margin-bottom-50 chengfenbiao"]/table/tbody/tr')
        ingreduents = []
        compositions = []
        for ingreduent in ingreduentList:
            try:
                component_name = ingreduent.xpath('th[1]/text()')[0].extract()
                security_risks = ingreduent.xpath('th[2]/text()')[0].extract()
                active_ingredient = ingreduent.xpath('th[3]/text()')[0].extract()
                risk_blain = ingreduent.xpath('th[4]/text()')[0].extract()
                prupose = ingreduent.xpath('th[5]/text()')[0].extract()
                composition_list = {"component_name": component_name, "security_risks": security_risks,
                                    "active_ingredient": active_ingredient, "risk_blain": risk_blain,
                                    "prupose": prupose}
                ingreduents.append(composition_list)
            except:
                component_name = ingreduent.xpath('td[1]/a/text()')[0].extract()
                try:
                    security_risks = ingreduent.xpath('td[2]/span/text()')[0].extract()
                except IndexError:
                    security_risks = ""

                active_ingredient = ingreduent.xpath('td[3]/img/@src').extract()
                if len(active_ingredient) == 0:
                    active_ingredient = ""
                else:
                    active_ingredient = active_ingredient[0]

                risk_blain = (ingreduent.xpath('td[4]/img/@src').extract())
                if len(risk_blain) == 0:
                    risk_blain = ""
                else:
                    risk_blain = risk_blain[0]

                purpose = (((ingreduent.xpath('td[5]/text()')[0].extract()).strip()).replace(' ', '')).replace('\n', ' ')
                composition_list = {"component_name": component_name, "security_risks": security_risks,
                                    "active_ingredient": active_ingredient, "risk_blain": risk_blain,
                                    "prupose": purpose}
                link = ingreduent.xpath('td[1]/a/@href')[0].extract()
                composition_url = 'https://www.bevol.cn' + link
                ingreduents.append(composition_list)
                ingredient_overview = bevolSpider.detail_info(composition_url)
                composition = {"component_name": component_name, "prupose": purpose,
                               "security_risks": security_risks, "ingredient_overview": ingredient_overview}
                compositions.append(composition)
        item['cosmetics_ingredients'] = json.dumps(ingreduents, ensure_ascii=False)
        item['compositions'] = json.dumps(compositions, ensure_ascii=False)
        yield item

    def detail_info(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html5lib")
        try:
            ingredient_overview = soup.select('div.component-info-box p')[0].text
        except IndexError:
            ingredient_overview = ""
        ingredient_overview = ingredient_overview.replace('\n', '')
        return ingredient_overview
