# -*- coding: utf-8 -*-


import scrapy
from ..items import CarItem
from scrapy_splash import SplashRequest
import re
import time
from .. import autohome

script = """
function main(splash)
    splash.images_enabled = false
    splash:go("https://www.autohome.com.cn")
    splash:wait(5)
end
"""


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["autohome.com.cn"]
    url = 'https://www.autohome.com.cn/grade/carhtml/'

    def start_requests(self):
        letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        for lett in letters:
            yield scrapy.Request(url=self.url+lett+'.html', callback=self.parse, meta={'splash': {
                'args': {'lua_source': script},
                'endpoint': 'render.html'
                }
            })

    def parse(self, response):
        for sel in response.xpath('body'):
            item = CarItem()
            brandList = sel.xpath('dl')
            carList = sel.xpath('dl/dd/ul[@class="rank-list-ul"]/li[contains(@id,"s")]')
            for brand in brandList:
                item['carBrand'] = brand.xpath('dd/div[@class="h3-tit"]/a/text()').extract()
            for cars in carList:
                    item['cars'] = cars.xpath('h4/a/text()').extract()
                    item['link'] = cars.xpath('h4/a/@href')[0].extract()
                    url = response.urljoin(item['link'])
                    yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('//div[@class="carseries-main"]/div[@class="series-list"]')
        item = CarItem()
        if len(detail) > 0:
            names = detail.xpath('div[@class="series-content"]/div[@id="specWrap-2"]/dl/dd/div[@class="spec-name"]/div[@class="name-param"]')
            for name in names:
                name = name.xpath('p')[0]
                item['carId'] = name.xpath('@data-gcjid').extract()
                item['carName'] = name.xpath('a/text()').extract()
                item['link'] = name.xpath('a/@href')[0].extract()
                url = response.urljoin(item['link'])
                yield scrapy.Request(url, meta={'carId': item['carId']}, callback=self.parse_article_detail)
        else:
            detail = response.xpath('//div[@class="title"]/div[@class="title-content"]')
            names = detail.xpath('div')
            for name in names:
                name = name.xpath('div[@class="models"]/div[@class="modelswrap"]/div/div/table/./tr/td[@class="name_d"]/div/a')
                for n in name:
                    item['carName'] = n.xpath('text()').extract()
                    item['link'] = n.xpath('@href')[0].extract()
                    item['carId'] = item['link'][5:-1]
                    if isinstance(item['carId'], str):
                        item['carId'] = int(item['carId'])
                    else:
                        item['carId'] = int(item['carId'][0])
                    url = response.urljoin(item['link'])
                    yield scrapy.Request(url, meta={'carId': item['carId']}, callback=self.parse_article_detail)

    def parse_article_detail(self, response):
        detail = response.xpath('//div[@class="container"]')
        item = CarItem()
        item['carId'] = response.meta['carId']
        item['carBrand'] = detail.xpath('div[@class="container athm-sub-nav article-sub-nav"]/div[@class="athm-sub-nav__car"]/div[@class="athm-sub-nav__car__name"]/a/text()')[0].extract()
        item['carBrand'] = item['carBrand'][:len(item['carBrand'])-1]
        item['cars'] = detail.xpath('div[@class="container athm-sub-nav article-sub-nav"]/div[@class="athm-sub-nav__car"]/div[@class="athm-sub-nav__car__name"]/a/h1/text()')[0].extract()
        item['carName'] = detail.xpath('div[@class="carspec-wrapper"]/div[@class="carspec-main"]/div[@class="spec-information"]/div[@class="information-tit"]/h2/text()')[0].extract()
        baseInfo = detail.xpath('div[@class="carspec-wrapper"]/div[@class="carspec-main"]/div[@class="spec-information"]/div[@class="information-con"]/div[@class="information-summary"]/div[@class="spec-baseinfo"]/ul[@class="baseinfo-list"]/li')
        item['link'] = baseInfo[8].xpath('a/@href')[0].extract()
        url = response.urljoin(item['link'])

        yield SplashRequest(url, meta={'carId': item['carId'], 'manufacturer': item['carBrand'],
                                       'cars': item["cars"], 'carName': item['carName']},
                            callback=self.parse_article_config, args={'wait': 5})

    def parse_article_config(self, response):
        html = response.body
        html = str(html.decode('utf-8'))
        item = CarItem()
        try:
            item['type_id'] = int(response.meta["carId"])
        except TypeError:
            item['type_id'] = int(response.meta["carId"][0])

        time.sleep(3)
        info = autohome.fetchCarInfo(html)
        detail = info[item['type_id']]
        for key in detail:
            item["%s" % key] = detail[key]

        item['brand_name'] = response.meta["manufacturer"]
        item['series_name'] = response.meta["cars"]
        item['car_name'] = item['series_name'] + " " + response.meta["carName"]
        yield item
        pass



