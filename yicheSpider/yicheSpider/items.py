# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YichespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    market_price_str = scrapy.Field()              # 厂商指导价
    market_time = scrapy.Field()                   # 上市时间
    car_level_str = scrapy.Field()                 # 车型级别
    car_struct = scrapy.Field()                    # 车身形式
    energy_type_str = scrapy.Field()               # 动力类型
    engine = scrapy.Field()                        # 发动机
    max_power = scrapy.Field()                     # 最大功率(kW)
    max_torque = scrapy.Field()                    # 最大扭矩(N・m)
    gearbox = scrapy.Field()                       # 变速箱
    mixed_fuel_consumption = scrapy.Field()        # 混合工况油耗
    speedup_time = scrapy.Field()                  # 0-100km加速时间[s]
    max_speed = scrapy.Field()                     # 最高车速(km/h)
    environmental_standard = scrapy.Field()        # 环保标准
    quality_guarantee = scrapy.Field()             # 保修政策
    car_size = scrapy.Field()                      # 长*宽*高(mm)
    shaft_distance = scrapy.Field()                # 轴距(mm)
    total_weight = scrapy.Field()                  # 整备质量(kg)
    seats = scrapy.Field()                         # 座位数(个)
    cargo_vol = scrapy.Field()                     # 行李厢容积(L)
    fuel_vol = scrapy.Field()                      # 油箱容积(L)
    front_wheel_size = scrapy.Field()              # 前轮胎规格
    back_wheel_size = scrapy.Field()               # 后轮胎规格
    backup_wheel = scrapy.Field()                  # 备胎
    cc = scrapy.Field()                            # 排量(mL)
    engine_hp = scrapy.Field()                     # 最大马力(Ps)
    engine_rpm = scrapy.Field()                    # 最大功率转速(rpm)
    torque_rpm = scrapy.Field()                    # 最大扭矩转速(rpm)
    oil_drive = scrapy.Field()                     # 供油方式
    compress_rate = scrapy.Field()                 # 压缩比
    roz = scrapy.Field()                           # 燃油标号
    engine_start_stop = scrapy.Field()             # 发动机启停
    gears_type = scrapy.Field()                    # 变速箱类型
    gears_num = scrapy.Field()                     # 挡位个数
    drive_method = scrapy.Field()                  # 驱动方式






