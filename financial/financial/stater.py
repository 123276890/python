#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from scrapy import cmdline



# scrapy crawl itcast （itcast为爬虫名）
os.system("scrapy crawl mycShop")
os.system("scrapy crawl miaoyouche")
os.system("scrapy crawl maodou")
os.system("scrapy crawl huasheng")
# cmdline.execute("scrapy crawl mycShop".split())
# cmdline.execute("scrapy crawl miaoyouche".split())
# cmdline.execute("scrapy crawl maodou".split())
# cmdline.execute("scrapy crawl huasheng".split())
