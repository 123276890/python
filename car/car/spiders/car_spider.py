# -*- coding: utf-8 -*-


import scrapy
from ..items import CarItem
from scrapy_splash import SplashRequest
import re
import time
from .. import autohome
import demjson

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
            Lists = sel.xpath('dl')
            for list in Lists:
                item['brand_name'] = list.xpath('dt/div/a/text()')[0].extract()
                cars = list.xpath('dd/ul[@class="rank-list-ul"]/li[contains(@id,"s")]/h4/a/text()').extract()
                i = 0
                for car in cars:
                    item['cars'] = car
                    item['link'] = list.xpath('dd/ul[@class="rank-list-ul"]/li[contains(@id,"s")]/h4/a/@href')[i].extract()
                    url = response.urljoin(item['link'])
                    i += 1

                    yield scrapy.Request(url, meta={'brand_name': item['brand_name']}, callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('//div[@class="carseries-main"]/div[@class="series-list"]')
        item = CarItem()
        brand_name = response.meta['brand_name']
        if len(detail) > 0:
            names = detail.xpath('div[@class="series-content"]/div[@id="specWrap-2"]/dl/dd/div[@class="spec-name"]/div[@class="name-param"]')
            for name in names:
                name = name.xpath('p')[0]
                item['carId'] = name.xpath('@data-gcjid').extract()
                item['carName'] = name.xpath('a/text()').extract()
                item['link'] = name.xpath('a/@href')[0].extract()
                url = response.urljoin(item['link'])
                if isinstance(item['carId'], str):
                    item['carId'] = int(item['carId'])
                else:
                    item['carId'] = int(item['carId'][0])

                yield scrapy.Request(url, meta={'carId': item['carId'], 'brand_name': brand_name}, callback=self.parse_article_detail)

        else:
            detail = response.xpath('//div[@class="title"]/div[@class="title-content"]')
            names = detail.xpath('div')
            for name in names:
                name = name.xpath('div[@class="models"]/div[@class="modelswrap"]/div/div/table/./tr/td[@class="name_d"]/div/a')
                for n in name:
                    item['carName'] = n.xpath('text()').extract()
                    item['link'] = n.xpath('@href')[0].extract()
                    item['carId'] = item['link'][5:-1]
                    url = response.urljoin(item['link'])
                    if isinstance(item['carId'], str):
                        item['carId'] = int(item['carId'])
                    else:
                        item['carId'] = int(item['carId'][0])

                    yield scrapy.Request(url, meta={'carId': item['carId'], 'brand_name': brand_name}, callback=self.parse_article_detail)

    def parse_article_detail(self, response):
        detail = response.xpath('//div[@class="container"]')
        item = CarItem()
        brand_name = response.meta['brand_name']
        item['carId'] = response.meta['carId']
        item['market_price_str'] = detail.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/dl[1]/dd[3]/span[1]/text()')[0].extract()
        item['market_price_str'] = item['market_price_str'].split("：")
        if item['market_price_str'][1] == "暂无":
            item['market_price_str'] = item['market_price_str'][1]
        else:
            item['market_price_str'] = item['market_price_str'][1] + "万元"
        item['carBrand'] = detail.xpath('div[@class="container athm-sub-nav article-sub-nav"]/div[@class="athm-sub-nav__car"]/div[@class="athm-sub-nav__car__name"]/a/text()')[0].extract()
        item['carBrand'] = item['carBrand'][:len(item['carBrand'])-1]
        item['cars'] = detail.xpath('div[@class="container athm-sub-nav article-sub-nav"]/div[@class="athm-sub-nav__car"]/div[@class="athm-sub-nav__car__name"]/a/h1/text()')[0].extract()
        item['carName'] = detail.xpath('div[@class="carspec-wrapper"]/div[@class="carspec-main"]/div[@class="spec-information"]/div[@class="information-tit"]/h2/text()')[0].extract()
        baseInfo = detail.xpath('div[@class="carspec-wrapper"]/div[@class="carspec-main"]/div[@class="spec-information"]/div[@class="information-con"]/div[@class="information-summary"]/div[@class="spec-baseinfo"]/ul[@class="baseinfo-list"]/li')
        item['link'] = baseInfo[8].xpath('a/@href')[0].extract()
        url = response.urljoin(item['link'])

        yield SplashRequest(url, meta={'carId': item['carId'], 'manufacturer': item['carBrand'],
                                       'cars': item["cars"], 'carName': item['carName'],
                                       'price': item['market_price_str'],  'brand_name': brand_name},
                            callback=self.parse_article_config, args={'wait': 5})

    def parse_article_config(self, response):
        html = response.body
        html = str(html.decode('utf-8'))
        item = CarItem()

        time.sleep(0.1)
        infos = autohome.fetchCarInfo(html)
        i = 0
        for info in infos:
            item['type_id'] = int(info)
            detail = infos[item['type_id']]
            for key in detail:
                item["%s" % key] = detail[key]

            if item['car_name'] == "-":
                i += 1
                continue
            item['brand_name'] = response.meta['brand_name']
            item['manufacturer'] = response.meta["manufacturer"]
            item['series_name'] = response.meta["cars"]
            prices = response.xpath('//*[@id="tr_2000"]/td')
            p = []
            for price in prices:
                try:
                    price = price.xpath('div/text()').extract()
                    p.append(price)
                except:
                    pass
            if len(p) == 0:
                break
            else:
                if len(p[i]) > 1:
                    p[i] = p[i][0] + p[i][1]
                else:
                    p[i] = p[i][0]
            item['market_price_str'] = p[i] + '万元'
            item['manufacturer'] = response.meta['manufacturer']
            yield item
            i += 1
        pass



