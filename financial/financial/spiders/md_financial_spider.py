# -*- coding: utf-8 -*-

import scrapy
from ..items import FinancialItem
from scrapy_splash import SplashRequest
import requests
import json
import re


class func():
    # 价格转换 例6.58万->65800
    def conversion_price(p):
        p = p.replace('万', '')
        p = int(float(p) * 10000)
        return p

class mdFinancialSpider(scrapy.Spider):
    name = "maodou"
    allowed_domains = ["www.maodou.com"]
    url = 'https://www.maodou.com'

    def start_requests(self):
        yield SplashRequest(url=self.url + '/sapi/category/getAllBrand', callback=self.parse, meta={'splash': {
                    'endpoint': 'render.html'
                    }
        })

    def parse(self, response):
        detail = eval(re.compile(r'\{.*\}').findall(response.text)[0])
        datas = detail['data']
        item = FinancialItem()
        for d in datas:
            data = datas[d]
            for base in data:
                item['brand_name'] = base['name']
                url = 'https://www.maodou.com/car/list/' + base['url']
                yield SplashRequest(url, callback=self.parse_car, meta={'splash': {
                    'endpoint': 'render.html'}, 'brand': item['brand_name']})

    def parse_car(self, response):
        detail = response.xpath('/html/body/div[2]/div/div[2]/div[3]')
        item = FinancialItem()
        item['brand_name'] = response.meta['brand']
        if len(detail) > 0:
            carList = detail.xpath('div[@id="models-list"]/div[1]/a')
            for car in carList:
                item['original_id'] = car.xpath('@data-id')[0].extract()
                item['model_name'] = car.xpath('div[2]/h2/span/text()')[0].extract()
                url = car.xpath('@href')[0].extract()
                yield SplashRequest(url, callback=self.parse_detail, meta={'splash': {
                    'endpoint': 'render.html'}, 'brand': item['brand_name'], 'oId': item['original_id'],
                    'mName': item['model_name']
                })
        else:
            pass

    def parse_detail(self, response):
        detail = response.xpath('//*[@id="banner"]/div/div[2]')
        item = FinancialItem()
        item['original_id'] = response.meta['oId']
        item['model_name'] = response.meta['mName']
        item['brand_name'] = response.meta['brand']
        item['guidance_price'] = ((detail.xpath('p/text()')[0].extract()).split('：'))[1]
        item['guidance_price'] = func.conversion_price(item['guidance_price'])
        plan = detail.xpath('div[1]')
        pros = []
        payment = plan.xpath('div[2]/ul/li/text()').extract()
        for p in payment:
            pros.append(p)
        pass