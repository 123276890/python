# -*- coding: utf-8 -*-

import scrapy
from ..items import FinancialItem
from scrapy_splash import SplashRequest
import requests
import json
import re
import time


class func():
    # 价格转换 例6.58万->65800
    def conversion_price(p):
        p = p.replace('万', '')
        p = int((float(p) + 10**-5) * 10000)
        return p


class hsFinancialSpider(scrapy.Spider):
    name = "huasheng"
    allowed_domains = ["www.huashenghaoche.com"]
    url = 'https://www.huashenghaoche.com/hshcweb/shanghai'

    def start_requests(self):
        for i in range(1, 9):
            yield SplashRequest(url=self.url + '/list/p' + str(i) + '.html', callback=self.parse, meta={'splash': {
                        'endpoint': 'render.html'
                        }
            })

    def parse(self, response):
        item = FinancialItem()
        detail = response.xpath('/html/body/div[2]/div[3]/div[2]/div[1]')
        carList = detail.xpath('a')
        for car in carList:
            url = 'https://www.huashenghaoche.com' + car.xpath('@href')[0].extract()
            item['original_id'] = car.xpath('div[1]/@data-carid')[0].extract()
            item['model_name'] = car.xpath('p[1]/text()')[0].extract()
            item['guidance_price'] = car.xpath('p[2]/span/text()')[0].extract()
            yield SplashRequest(url, callback=self.parse_detail, args={'wait': 3}, meta={'splash': {
                'endpoint': 'render.html'}, 'oId': item['original_id'], 'mName': item['model_name'],
                'price': item['guidance_price']
            })

    def parse_detail(self, response):
        time.sleep(3)
        detail = response.xpath('/html/body/div[3]/div[1]/div[2]')
        item = FinancialItem()
        item['original_id'] = response.meta['oId']
        item['model_name'] = response.meta['mName']
        item['original_url'] = response.url
        item['brand_name'] = (item['model_name'].split())[0]
        item['series_name'] = (item['model_name'].split())[1]
        item['guidance_price'] = func.conversion_price(response.meta['price'])
        plans = detail.xpath('div[2]/ul')
        payment = []
        for plan in plans:
            first_price = func.conversion_price(plan.xpath('li[1]/p/text()')[0].extract())
            month_price = plan.xpath('li[2]/p/text()')[0].extract()
            period = plan.xpath('li[3]/p/text()')[0].extract()
            schemes = {'period': period, 'first_price': first_price, 'month_price': month_price}
            payment.append(schemes)
        item['riders'] = {"车源保障": ["花生好车车源由各大汽车品牌厂商直接提供，车源品质有保障"],
                          "购车资料": ["购车需要提供二代身份证、驾驶证、征信报告"],
                          "赠送保险": ["花生好车送1年保险，包含交强险、车损险、第三者责任险（100万）、车身人员责任险、不计免赔特约险、自然险、 涉水损失险，提供盗抢险服务"],
                          "还款": ["购车后通过提供绑定的银行卡按时还款"],
                          "车辆归属": ["结清购车费用前，车辆以及车牌所有权归花生好车，结清全部费用后即可办理车辆过户"],
                          "上牌": ["花生好车负责办理车辆上牌，您无需到场、无需额外支付费用"],
                          "免手续费": ["除综合保证金外，用户无需支付其他额外费用"]}
        item['riders'] = json.dumps(item['riders'], ensure_ascii=False)

        item['schemes'] = payment
        item['schemes'] = json.dumps(item['schemes'])

        item['source_id'] = '7'
        item['give_license_ex'] = '花生好车负责办理车辆上牌，您无需到场、无需额外支付费用'
        item['give_license'] = '1'
        item['give_insurance'] = '1'
        item['give_insurance_ex'] = '送一年保险'
        item['give_purchase_tax_ex'] = '含购置税'
        item['give_purchase_tax'] = '1'
        item['pickup_mode'] = '到店提车'
        yield item
