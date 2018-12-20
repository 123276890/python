# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinancialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    original_id = scrapy.Field()                            # 原系统ID
    original_url = scrapy.Field()                           # 原系统url
    model_name = scrapy.Field()                             # 车型名
    series_name = scrapy.Field()                            # 车系名
    brand_name = scrapy.Field()                             # 品牌名
    source_id = scrapy.Field()                              # 数据来源ID 弹个车 2
    model_version = scrapy.Field()                          # 版本名
    guidance_price = scrapy.Field()                         # 指导价
    selling_price = scrapy.Field()                          # 售价
    service_charge = scrapy.Field()                         # 服务费
    deposit = scrapy.Field()                                # 保证金
    front_money = scrapy.Field()                            # 定金
    licensing_price = scrapy.Field()                        # 上牌费
    gps_price = scrapy.Field()                              # gps安装费
    pickup_mode = scrapy.Field()                            # 提货方式
    pickup_city = scrapy.Field()                            # 提货城市
    give_purchase_tax = scrapy.Field()                      # 是否赠送购置税
    give_purchase_tax_ex = scrapy.Field()
    give_insurance = scrapy.Field()                         # 是否赠送保险
    give_insurance_ex = scrapy.Field()
    give_license = scrapy.Field()                           # 是否赠送车牌
    give_license_ex = scrapy.Field()
    give_maintain = scrapy.Field()                          # 是否赠送保养
    give_maintain_ex = scrapy.Field()
    riders = scrapy.Field()                                 # 附加条款
    images = scrapy.Field()                                 # 图片
    schemes = scrapy.Field()                                # 金融方案
    lisense_city = scrapy.Field()                           # 上牌城市
    shops = scrapy.Field()                                  # 门店


class shopItem(scrapy.Item):
    source_id = scrapy.Field()                           # 数据来源ID
    original_id = scrapy.Field()                         # 店铺id
    shop_type = scrapy.Field()                           # 店铺类型 0:4S店，1:融资方案店
    shop_name = scrapy.Field()                           # 店铺名称
    shop_province = scrapy.Field()                       # 所在省份
    shop_city = scrapy.Field()                           # 所在城市
    shop_district = scrapy.Field()                       # 所在区
    shop_address = scrapy.Field()                        # 地址
    shop_telphone = scrapy.Field()                       # 店铺电话
