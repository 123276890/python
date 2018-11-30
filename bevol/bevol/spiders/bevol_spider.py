# -*- coding: utf-8 -*-


import scrapy
from scrapy_splash import SplashRequest
from ..items import BevolItem
import re


class bevolSpider(scrapy.Spider):
    name = "bevol"
    allowed_domains = ["www.bevol.cn"]
    url = 'https://www.bevol.cn/product'

    def start_requests(self):
        pageList = [6, 7, 8, 9, 10, 11, 12, 13, 15, 20, 47, 30, 38]
        for i in pageList:
            yield SplashRequest(url=self.url + '?category=' + str(i), callback=self.parse, args={'wait': 2}, meta={'splash': {
                        'endpoint': 'render.html'
                        }
            })

    def parse(self, response):
        page = response.xpath('/html/body/div[2]/div[3]/div[4]/div/a[4]/text()')[0].extract()
        url = (response.url).split('?')
        i = 1
        while i <= int(page):
            yield SplashRequest(url=url[0] + '?v=2.0' + '&' + url[1] + '&p=' + str(i), callback=self.parse_list, args={'wait': 2},
                                meta={'splash': {
                                    'endpoint': 'render.html'
                                }
                            })
            i += 1

    def parse_list(self, response):
        list = response.xpath('/html/body/div[2]/div[3]/div[1]/div[3]/ul/a')
        item = BevolItem()
        for l in list:
            url = 'https://www.bevol.cn' + l.xpath('@href')[0].extract()
            item['cosmetics_name'] = l.xpath('@title')[0].extract()
            item['cosmetics_id'] = re.compile(r'\/.*?\/(.*)\.(html)').search(l.xpath('@href')[0].extract()).group(1)
            yield SplashRequest(url, callback=self.parse_detail, args={'wait': 2}, meta={'splash': {
                                    'endpoint': 'render.html'}, 'id': item['cosmetics_id'], 'name': item['cosmetics_name']
                            })

    def parse_detail(self, response):
        item = BevolItem()
        item['cosmetics_name'] = response.meta['name']
        item['cosmetics_id'] = response.meta['id']
        detail = response.xpath('/html/body/div[2]/div[4]')
        pass