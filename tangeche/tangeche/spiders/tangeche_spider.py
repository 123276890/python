# -*- coding: utf-8 -*-


import scrapy
from ..items import TangecheItem
from scrapy_splash import SplashRequest
import requests
import json
import time


class TangecheSpider(scrapy.Spider):
    name = "tangeche"
    allowed_domains = ["www.tangeche.com"]
    url = 'https://www.tangeche.com/buy'

    def start_requests(self):
        for i in range(1, 8):
            yield SplashRequest(url=self.url + "?page=" + str(i), callback=self.parse, args={'wait': 4}, meta={'splash': {
                    'endpoint': 'render.html'
                    }
                })

    def parse(self, response):
        details = response.xpath('//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div/div/div')
        item = TangecheItem()
        for detail in details:
            link = detail.xpath('a/@href')[0].extract()
            carId = (detail.xpath('a/@href')[0].extract()).split("/")
            item['original_id'] = carId[3]
            url = 'https://www.tangeche.com' + link
            yield scrapy.Request(url, callback=self.parse_detail, meta={'carId': item['original_id']})

    def parse_detail(self, response):
        item = TangecheItem()
        item['original_id'] = response.meta['carId']
        content = {'modelCode': item['original_id']}
        url = 'https://leaseconsumer.souche.com//v1/newCarDetailApi/getLayerdFinanceInfoList.json'
        result = requests.post(url, data=content)
        url2 = 'https://leaseconsumer.souche.com//v1/newCarDetailApi/getModelDetailForPC.json'
        result2 = requests.post(url2, data=content)
        financialPlan = (json.loads(result.text))['data'][0]
        financeInfo = financialPlan['layeredFinanceInfo']
        carInfo = (json.loads(result2.text))['data']['carInfo']
        financeInfoStandard = (json.loads(result2.text))['data']['financeInfoList'][0]
        item['source_id'] = 2
        item['brand_name'] = carInfo['brandName']
        item['series_name'] = carInfo['seriesName']
        item['model_name'] = carInfo['modelName']
        item['guidance_price'] = int(carInfo['guidePrice']/100)
        item['service_charge'] = int(financeInfoStandard['deliveryCarServiceCost']/100)
        item['pickup_mode'] = "到店提车"
        leaseTags = financeInfoStandard['leaseTags']
        if leaseTags[0] == '含购置税':
            item['give_purchase_tax_ex'] = leaseTags[0]
            item['give_purchase_tax'] = '1'
        else:
            pass
        item['give_insurance_ex'] = '送1年保险'
        item['give_insurance'] = '1'

        item['give_license'] = '1'
        item['give_license_ex'] = '上牌手续由弹个车负责办理，客户无需支付任何费用'
        item['riders'] = {'资料': ['您只需提供有效驾驶证'],
                          '保险': ['弹个车送1年车险，含交强险、第三者责任险（30万）、车上人员责任险（司机）、车损险及以上几项险种的不计免赔险；提供盗抢险和涉水险理赔服务。如需增加其他保险险种，可联系顾问办理，增加险种费用由用户自己承担'],
                          '还款': ['购车后每月还款通过支付宝的余额宝或绑定的银行卡内自动扣款'],
                          '车辆归属': ['前1年用车期间，车辆及车牌所有权归属弹个车平台'],
                          '上牌': ['上牌手续由弹个车负责办理，客户无需支付任何费用'],
                          '购置税': ['弹个车方案已含购置税，您无需支付额外费用']}
        item['riders'] = json.dumps(item['riders'], ensure_ascii=False)
        schemes = []
        i = 0
        for f in financeInfo:
            first_price = financeInfo[i]['prepaidAmount']
            month_price = financeInfo[i]['installmentStr']
            first_ratio = int(financeInfo[i]['prepaidRate']/100)
            final_month_price = financialPlan['finalPayInstallment']
            final_payment = financialPlan['allFinalPayment']
            period = '12'
            final_period = '36'
            scheme = {"period": period,
                                "first_price": first_price,
                                "month_price": month_price,
                                "final": [{"final_month_price": final_month_price,
                                           "final_payment": final_payment,
                                           "final_period": final_period}],
                                "first_ratio": first_ratio}
            schemes.append(scheme)
            i += 1
        item['schemes'] = json.dumps(schemes)
        if item['original_id'].count('-') > 0:
            item['original_id'] = (item['original_id'].split("-"))[0]
        item['original_url'] = response.url
        yield item