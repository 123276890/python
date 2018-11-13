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
    susp_front_type = scrapy.Field()               # 前悬架类型
    susp_back_type = scrapy.Field()                # 后悬架类型
    variable_susp = scrapy.Field()                 # 可调悬架
    front_brake = scrapy.Field()                   # 前轮制动器类型
    back_brake = scrapy.Field()                    # 后轮制动器类型
    park_brake = scrapy.Field()                    # 驻车制动类型
    structure = scrapy.Field()                     # 车体结构
    front_diff_lock = scrapy.Field()               # 限滑差速器/差速锁
    anti_lock = scrapy.Field()                     # ABS防抱死
    bfd = scrapy.Field()                           # 制动力分配(EBD/CBC等)
    bas = scrapy.Field()                           # 制动辅助(EBA/BAS/BA等)
    tcs = scrapy.Field()                           # 牵引力控制(ASR/TCS/TRC等)
    stable_control = scrapy.Field()                # 车身稳定控制(ESC/ESP/DSC等)
    seat_srs = scrapy.Field()                      # 主/副驾驶座安全气囊
    side_airbag = scrapy.Field()                   # 前/后排侧气囊
    head_srs = scrapy.Field()                      # 侧安全气帘
    knee_srs = scrapy.Field()                      # 膝部气囊
    seat_air_bag = scrapy.Field()                  # 安全带气囊
    central_air_bag = scrapy.Field()               # 后排中央气囊
    tire_pres_monitor = scrapy.Field()             # 胎压监测
    zero_tire_pres = scrapy.Field()                # 零胎压继续行驶
    isofix = scrapy.Field()                        # 后排儿童座椅接口
    cruise_ctrl = scrapy.Field()                   # 定速巡航
    ldw = scrapy.Field()                           # 车道保持
    bsa = scrapy.Field()                           # 并线辅助
    abs = scrapy.Field()                           # 主动刹车/碰撞报警
    tired_drive = scrapy.Field()                   # 疲劳提醒
    auto_park_in = scrapy.Field()                  # 自动泊车
    control_park_in = scrapy.Field()               # 遥控泊车
    auto_drive = scrapy.Field()                    # 自动驾驶辅助
    auto_park = scrapy.Field()                     # 自动驻车
    hac = scrapy.Field()                           # 上坡辅助
    hdc = scrapy.Field()                           # 陡坡缓降
    nvs = scrapy.Field()                           # 夜视系统
    vgrs = scrapy.Field()                          # 可变齿比转向
    radar = scrapy.Field()                         # 前/后驻车雷达
    reverse_video = scrapy.Field()                 # 倒车影像
    drive_model = scrapy.Field()                   # 驾驶模式选择
    headlamps = scrapy.Field()                     # 前大灯
    led_beam = scrapy.Field()                      # LED日间行车灯
    automatic_headlight = scrapy.Field()           # 自动大灯
    front_fog_lamp = scrapy.Field()                # 前雾灯
    light_height_adjt = scrapy.Field()             # 大灯高度可调
    light_clean_dev = scrapy.Field()               # 大灯清洗装置
    skylight_type = scrapy.Field()                 # 天窗类型
    power_window = scrapy.Field()                  # 前/后电动车窗
    e_adjt_rearview = scrapy.Field()               # 后视镜电动调节
    heat_rearview = scrapy.Field()                 # 后视镜加热
    mirror_mem = scrapy.Field()                    # 后视镜记忆
    power_mirror = scrapy.Field()                  # 电动折叠
    dimming_mirror = scrapy.Field()                # 内/外后视镜自动防眩目
    stream_media_rearview = scrapy.Field()         # 流媒体后视镜
    side_priv_glass = scrapy.Field()               # 隐私玻璃
    side_abat_vent = scrapy.Field()                # 后排侧遮阳帘
    abat_vent = scrapy.Field()                     # 后遮阳帘
    before_the_wiper = scrapy.Field()              # 前雨刷器
    after_the_wiper = scrapy.Field()               # 后雨刷器
    electric_door_absorption = scrapy.Field()      # 电吸门
    slide_door = scrapy.Field()                    # 电动侧滑门
    electric_suitcase = scrapy.Field()             # 电动行李箱
    roof_rack = scrapy.Field()                     # 车顶行李架
    e_ctrl_lock = scrapy.Field()                   # 中控锁
    intelligent_key = scrapy.Field()               # 智能钥匙
    remote_control = scrapy.Field()                # 远程遥控功能
    tail = scrapy.Field()                          # 尾翼
    sport_package = scrapy.Field()                 # 运动外观套件
    interior_materials = scrapy.Field()            # 内饰材质
    interior_atmosphere_light = scrapy.Field()     # 车内氛围灯
    sun_shield = scrapy.Field()                    # 遮阳板化妆镜
    steering_material = scrapy.Field()             # 方向盘材质
    functional_steer = scrapy.Field()              # 多功能方向盘
    steer_adjt = scrapy.Field()                    # 方向盘调节
    steer_heat = scrapy.Field()                    # 方向盘加热
    steer_shift = scrapy.Field()                   # 方向盘换挡
    before_air = scrapy.Field()                    # 前排空调
    back_air = scrapy.Field()                      # 后排空调
    sweet_system = scrapy.Field()                  # 香氛系统

































