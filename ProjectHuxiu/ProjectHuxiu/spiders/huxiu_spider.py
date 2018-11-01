# -*- coding: utf-8 -*-

from ..items import HuxiuItem
import scrapy
from scrapy import Spider, Request
from scrapy_splash import SplashTextResponse

script = """
        function main(splash)
          splash.images_enabled = false
          splash:go("https://www.huxiu.com/index.php")
          splash:wait(5)
          js = string.format("document.getElementsByClassName('get-mod-more transition js-get-mod-more-list')[0].click()")
          splash:runjs(js)
          splash:wait(5)
        end
"""

class HuxiuSpider(scrapy.Spider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    # start_urls = ['https://www.huxiu.com/index.php']
    url = "https://www.huxiu.com/index.php"

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse, meta={'splash': {
            'args': {'lua_source': script},
            'endpoint': 'render.html'}
        })

    def parse(self, SplashTextResponse):
        for sel in SplashTextResponse.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt index-article-list-yh"]'):
            item = HuxiuItem()
            item['title'] = sel.xpath('h2/a/text()')[0].extract()
            item['link'] = sel.xpath('h2/a/@href')[0].extract()
            url = SplashTextResponse.urljoin(item['link'])
            item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract().strip()
            # print(item['title'], item['link'], item['desc'])
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('//div[@class="article-wrap"]')
        item = HuxiuItem()
        item['title'] = detail.xpath('h1/text()')[0].extract().strip()
        item['link'] = response.url

        patha = detail.xpath('div[@class="article-author"]/div[@class="column-link-box"]/span[@class="article-time pull-left"]/text()')
        if patha:
            item['posttime'] = patha[0].extract()
            pass
        else:
            item['posttime'] = detail.xpath('div[@class="article-author"]/span[@class="article-time"]/text()')[0].extract()
            pass

        print(item['title'], item['link'], item['posttime'])
        yield item
