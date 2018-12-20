#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy import cmdline

# scrapy crawl itcast （itcast为爬虫名）
cmdline.execute("scrapy crawl mycShop".split())
# cmdline.execute("scrapy crawl miaoyouche".split())
# cmdline.execute("scrapy crawl maodou".split())
# cmdline.execute("scrapy crawl huasheng".split())
