# -*- coding: utf-8 -*-

import scrapy, re, json, requests, time
from ..items import shopItem
from  class_func import func


class mycShopSpider(scrapy.Spider):
    name = 'mycShop'
    allowed_domains = ["www.miaoyouche.com"]
    url = 'https://www.miaoyouche.com'

    def start_requests(self):
        yield scrapy.Request(url=self.url + '/store', callback=self.parse)

    def parse(self, response):
        now = int(round(time.time() * 1000))
        headers = {'Content-Type': "application/json; charset=UTF-8", 'platform': "PC", 'timestamp': str(now), 'Authorization': ""}
        content = {'pageSize': '10'}
        url = 'https://carlib.miaoyouche.com/api/myc-car/franc/franAll'
        result = requests.post(url, headers=headers, data=json.dumps(content))
        total_page = (json.loads(result.text))['data']['totalPage']
        for i in range(1,total_page):
            content = {'pageSize': '10', 'currentPage': str(i)}
            result = requests.post(url, headers=headers, data=json.dumps(content))
            rowData = (json.loads(result.text))['data']['rows']
            for row in rowData:
                item = shopItem()
                item['source_id'] = '12'
                item['original_id'] = row['id']
                item['shop_type'] = '1'
                item['shop_name'] = row['franchiseeName']
                item['shop_address'] = row['detailAddress']
                item['shop_telphone'] = row['francTelephone']
                provinceCity = func.provinceCity(item['shop_address'])
                if len(provinceCity) > 2:
                    item['shop_province'] = provinceCity[0]
                    item['shop_city'] = provinceCity[1]
                    item['shop_district'] = provinceCity[2]
                elif len(provinceCity) > 1:
                    item['shop_province'] = provinceCity[0]
                    item['shop_city'] = provinceCity[1]
                else:
                    pass
                item['shop_type'] = '1'
                yield item

