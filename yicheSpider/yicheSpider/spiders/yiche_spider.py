# -*- coding: utf-8 -*-

import scrapy
import re
from ..items import YichespiderItem
from scrapy_splash import SplashRequest


class yicheSpider(scrapy.Spider):
    name = "yiche"
    allowed_domains = ["www.bitauto.com"]
    url = 'http://car.bitauto.com/tree_chexing'

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse, meta={'splash': {'args':{'endpoint':'render.html'}}})

    def parse(self, response):
        for sel in response.xpath('body'):
            item = YichespiderItem()