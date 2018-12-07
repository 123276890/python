# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BevolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    cosmetics_id = scrapy.Field()                                   # 产品id
    cosmetics_name = scrapy.Field()                                 # 产品名
    cosmetics_img = scrapy.Field()                                  # 产品图片
    cosmetics_absolute = scrapy.Field()                             # 进口备案
    cosmetics_star = scrapy.Field()                                 # 安全星级
    security_said = scrapy.Field()                                  # 安全说
    cosmetics_ingredients = scrapy.Field()                          # 产品成分表
    cosmetics_composition_name = scrapy.Field()                     # 产品成分名
    cosmetics_purpose = scrapy.Field()                              # 使用目的
    ingredient_overview = scrapy.Field()                            # 成分简介
    security_risks = scrapy.Field()                                 # 安全风险
    cosmetics_url = scrapy.Field()                                  # 产品url
    compositions = scrapy.Field()                                   # 成分
    category = scrapy.Field()                                       # 类别
