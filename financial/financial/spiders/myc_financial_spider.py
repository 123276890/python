# -*- coding: utf-8 -*-

import scrapy, re, json
from ..items import FinancialItem
from class_func import func


class mycFinancialSpider(scrapy.Spider):
    name = 'miaoyouche'
    allowed_domains = ["www.miaoyouche.com"]
    url = 'https://www.miaoyouche.com'

    def start_requests(self):
        for i in range(1, 12):
            yield scrapy.Request(url=self.url + '/www/car?curPage=' + str(i), callback=self.parse)

    def parse(self, response):
        carList = response.xpath('/html/body/div/div[@class="content"]/div/ul/li')
        for car in carList:
            link = car.xpath('a/@href')[0].extract()
            url = response.urljoin(link)
            carId = (re.compile(r'\d+').findall(link))[0]
            yield scrapy.Request(url, callback=self.detail_parse, meta={'carId': carId})

    def detail_parse(self, response):
        detail = response.xpath('/html/body/div/div[@class="mainbox"]/div[1]/div[@class="car_look"]/div[@class="car_right"]')
        item = FinancialItem()
        item['brand_name'] = detail.xpath('div[@class="info_title"]/span[@class="car-brand-name"]/text()')[0].extract()
        item['series_name'] = detail.xpath('div[@class="info_title"]/span[@class="car-series-name"]/text()')[0].extract()
        item['model_name'] = detail.xpath('div[@class="info_title"]/span[@class="car-type-name"]/text()')[0].extract()
        guidance_price = detail.xpath('div[@class="info_line2"]/div[@class="info_price"]/text()')[0].extract()
        item['guidance_price'] = func.conversion_price(guidance_price, '1')
        payments = []
        payment = detail.xpath('div[@class="info_line6"]/div[@class="pro_cont"]/ul/li/div/text()').extract()
        for p in payment:
            p = p.replace('%', '')
            payments.append(p)
        plan = detail.xpath('div[starts-with(@class,"period-item")]')
        schemes = []
        i = 0
        for p in plan:
            pl = p.xpath('div')
            for l in pl:
                first_price = l.xpath('div[1]/div[@class="l3_val"]/@data-val')[0].extract()
                first_price = func.price_reduce(first_price)
                month_price = l.xpath('div[2]/div[@class="l3_val"]/@data-val')[0].extract()
                month_price = func.price_reduce(month_price)
                period = l.xpath('div[3]/div[@class="l3_val"]/@data-val')[0].extract()
                first_ratio = payments[i]
                scheme = func.json_schemes(period, first_price, month_price, first_ratio)
                schemes.append(scheme)
                pass
            i += 1
        item['original_id'] = response.meta['carId']
        item['give_purchase_tax'] = '1'
        item['give_purchase_tax_ex'] = '含购置税'
        item['give_insurance_ex'] = '送一年保险'
        item['give_insurance'] = '1'
        item['give_license'] = '1'
        item['give_license_ex'] = '妙优车负责免费为您办理购车城市 或临近城市的汽车牌照,无需您到场'
        item['riders'] = {"资料": ["您只需提供有效驾驶证"],
                          "保险": ["妙优车送1年车险，含交强险、第三者责任险（30万）、车上人员责任险（司机）、车损险及以上几项险种的不计免赔险；提供盗抢险和涉水险理赔服务。如需增加其他保险险种，可联系顾问办理，增加险种费用由用户自己承担"],
                          "还款": ["购车后每月还款通过支付宝的余额宝或绑定的银行卡内自动扣款"],
                          "车辆归属": ["前1年用车期间，车辆及车牌所有权归属妙优车平台"],
                          "上牌": ["上牌手续由妙优车负责办理，客户无需支付任何费用"],
                          "购置税": ["妙优车方案已含购置税，您无需支付额外费用"]}
        item['riders'] = json.dumps(item['riders'], ensure_ascii=False)
        item['schemes'] = json.dumps(schemes)
        item['source_id'] = '12'
        yield item
