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
                yield SplashRequest(url, callback=self.parse_detail, args={'wait': 8}, meta={'splash': {
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
        item['guidance_price'] = detail.xpath('p/text()')[0].extract()
        item['guidance_price'] = item['guidance_price'].split('：')
        item['guidance_price'] = item['guidance_price'][1]
        item['guidance_price'] = func.conversion_price(item['guidance_price'])
        plan = detail.xpath('div[1]')
        pros = []       # 首付比例数组
        payPlans = []   # 方案数组
        payment = plan.xpath('div[2]/ul/li/text()').extract()
        i = 0
        for p in payment:
            p = p.replace('%首付', '')
            pros.append(p)
        while i < len(pros):
            j = i + 3
            pays = plan.xpath('div[%s]' % j)
            for p in pays:
                m = 1
                while m <= len(pays.xpath('div')):
                    first_price = func.conversion_price(p.xpath('div[%s]/div[1]/div[1]/p[2]/text()' % m)[0].extract())
                    month_price = (p.xpath('div[%s]/div[1]/div[2]/p[2]/text()' % m)[0].extract()).replace('元', '')
                    period = (p.xpath('div[%s]/div[1]/div[3]/p[2]/text()' % m)[0].extract()).replace('期', '')
                    first_ratio = pros[i]
                    pay = {'period': period, 'first_price': first_price, 'month_price': month_price, 'first_ratio': first_ratio}
                    payPlans.append(pay)
                    m += 1
            i += 1
        item['riders'] = {"购车所需资料": ["您只需要提供有效期内的驾驶证，并线上进行贷款资格审核"],
                          "还款": ["提车次月起通过绑定的银行卡按时还款"],
                          "车辆归属": ["在前4年用车期间，车辆以及车牌所有权归属毛豆，之后客户可选择在支付留购价后过户"],
                          "留购价": ["法律规定，在融资租赁关系终止后，承租人支付租赁物的残值或者合同约定价值之后获得租赁物的所有权。这个支付的价格就是留购价"],
                          "车源供应": ["毛豆新车均由各大汽车品牌厂商直接供应，车源品质有保障"],
                          "保险明细": ["毛豆送1年保险，包含交强险、第三者责任险30万、车损险、不计免赔险"],
                          "上牌": ["毛豆负责办理车辆上牌，您无需到现场和额外支付费用。"],
                          "购置税": ["首年费用已经包含购置税，您无需支付额外费用"]}
        item['riders'] = json.dumps(item['riders'], ensure_ascii=False)

        item['schemes'] = payPlans
        item['schemes'] = json.dumps(item['schemes'])

        item['give_license_ex'] = '毛豆负责办理车辆上牌，您无需到现场和额外支付费用'
        item['give_license'] = '1'
        item['give_insurance'] = '1'
        item['give_insurance_ex'] = '送一年保险'
        item['give_purchase_tax_ex'] = '含购置税'
        item['give_purchase_tax'] = '1'
        item['pickup_mode'] = '到店提车'
        try:
            item['service_charge'] = plan.xpath('div[6]/div/div[1]/text()')[0].extract()
        except:
            try:
                item['service_charge'] = plan.xpath('div[7]/div/div[1]/text()')[0].extract()
            except:
                item['service_charge'] = plan.xpath('div[8]/div/div[1]/text()')[0].extract()
        item['service_charge'] = re.compile(r'[0-9]\d*').findall(item['service_charge'])[0]
        item['series_name'] = (item['model_name'].split())[0]
        item['source_id'] = '4'
        item['original_url'] = response.url
        yield item