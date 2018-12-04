# -*- coding: utf-8 -*-


import scrapy
from scrapy_splash import SplashRequest
from ..items import BevolItem
import re
import json
import time
import requests
from lxml import etree



class bevolSpider(scrapy.Spider):
    name = "bevol"
    allowed_domains = ["www.bevol.cn"]
    url = 'https://www.bevol.cn/product'

    def start_requests(self):
        pageList = [6, 7, 8, 9, 10, 11, 12, 13, 15, 20, 47, 30, 38]
        for i in pageList:
            yield SplashRequest(url=self.url + '?category=' + '9', callback=self.parse, args={'wait': 3}, meta={'splash': {
                        'endpoint': 'render.html'
                        }
            })

    def parse(self, response):
        time.sleep(2)
        page = response.xpath('/html/body/div[2]/div[3]/div[4]/div/a[4]/text()')[0].extract()
        url = (response.url).split('?')
        i = 1
        while i <= int(page):
            yield SplashRequest(url=url[0] + '?v=2.0' + '&' + url[1] + '&p=' + str(i), callback=self.parse_list, args={'wait': 3},
                                meta={'splash': {
                                    'endpoint': 'render.html'
                                }
                            })
            i += 1

    def parse_list(self, response):
        time.sleep(2)
        list = response.xpath('/html/body/div[2]/div[3]/div[1]/div[3]/ul/a')
        if len(list) > 0:
            item = BevolItem()
            for l in list:
                url = 'https://www.bevol.cn' + l.xpath('@href')[0].extract()
                item['cosmetics_name'] = l.xpath('@title')[0].extract()
                item['cosmetics_absolute'] = l.xpath('li/div[2]/p[@class="absolute p4"]/text()')[0].extract()
                item['cosmetics_absolute'] = item['cosmetics_absolute'].strip()
                item['cosmetics_id'] = re.compile(r'\/.*?\/(.*)\.(html)').search(l.xpath('@href')[0].extract()).group(1)
                yield SplashRequest(url, callback=self.parse_detail, args={'wait': 8}, meta={'splash': {
                                        'endpoint': 'render.html'}, 'id': item['cosmetics_id'],
                                        'name': item['cosmetics_name'], 'absolute': item['cosmetics_absolute']
                                })
        else:
            pass

    def parse_detail(self, response):
        time.sleep(2)
        item = BevolItem()
        item['cosmetics_name'] = response.meta['name']
        item['cosmetics_id'] = response.meta['id']
        detail = response.xpath('/html/body/div[2]/div[4]')
        starList = detail.xpath('div[1]/div[2]/div[1]/div[1]/img/@src').extract()
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
        ingreduentList = detail.xpath('div[1]/div[3]/table/tbody/tr')
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
                risk_blain = (ingreduent.xpath('td[4]/text()')[0].extract()).strip()
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
        time.sleep(2)
        response.encoding = 'utf-8'
        ingredient_overview = re.compile(r'\<div\s*class\=\"component-info-box\"\>\s*<p>(.*)</p>\s*</div>').search(response.text)
        ingredient_overview = ingredient_overview.group(1)
        return ingredient_overview
