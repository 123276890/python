# -*- coding: utf-8 -*-


import scrapy
from scrapy_splash import SplashRequest


class bevolSpider(scrapy.Spider):
    name = "bevol"
    allowed_domains = ["www.bevol.cn"]
    url = 'https://www.bevol.cn/product'

    def start_requests(self):
        pageList = [6, 7, 8, 9, 10, 11, 12, 13, 15, 20, 47, 30, 38]
        for i in pageList:
            yield SplashRequest(url=self.url + '?category=' + str(i), callback=self.parse, meta={'splash': {
                        'endpoint': 'render.html'
                        }
            })