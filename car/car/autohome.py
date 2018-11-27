# -*- coding: utf-8 -*-

import re
import json
from .items import CarItem
import time
import demjson


# 循环抓取数据
def GraspTheData(v, path, ret, key, dic):
    for value in v[path]:
        dealAutoHomeItemValue(value, ret, key, dic)


def NewAutoHomeCar(aid):
    c = CarItem()
    c['settings'] = "https://car.autohome.com.cn/config/spec/" + str(aid) + ".html"
    return c


def fetchCarInfo(html):
    time.sleep(2)
    car_info_datas = re.compile(r"<script>((?:.|\\n)*?)</script>").findall(html)
    js_matches = []
    dic = {}

    for strs in car_info_datas:
        strslist = []
        for s in strs:
            s = ord(s)
            strslist.append(s)
        if strs.find("try{document.") < 0:
            if len(strslist) > 500:
                js_matches.append(strs)

    for i, js in enumerate(js_matches):
        if i == 1:
            dic["config"] = getAutoHomeDict(js)
        elif i == 2:
            dic["option"] = getAutoHomeDict(js)
        else:
            pass

    # 基本参数组
    pos_start = html.find("var config =")
    if pos_start <= 0:
        pass
    str_base = html[pos_start:]
    pos_end = str_base.find('''\n''')
    if pos_end > len(str_base):
        pass
    str_base = str_base[13:pos_end - 1]

    # 选项配置参数组
    pos_start = html.find("var option =")
    if pos_start <= 0:
        pass
    str_option = html[pos_start:]
    pos_end = str_option.find('''\n''')
    if pos_end > len(str_option):
        pass
    str_option = str_option[13:pos_end - 1]

    # 外观颜色json
    pos_start = html.find("var color =")
    if pos_start <= 0:
        pass
    str_color = html[pos_start:]
    pos_end = str_color.find('''\n''')
    if pos_end > len(str_color):
        pass
    str_color = str_color[12:pos_end - 1]

    # 内饰颜色Json
    pos_start = html.find("var innerColor =")
    if pos_start <= 0:
        pass
    str_inner = html[pos_start:]
    pos_end = str_inner.find('''\n''')
    if pos_end > len(str_inner):
        pass
    str_inner = str_inner[16:pos_end - 1]

    # 车型ID抓取
    time.sleep(0.1)
    result = demjson.decode(str_base)["result"]["speclist"]
    ret = {}
    if type(result) != None and len(result) != 0:
        items = list(result)
        for item in items:
            key_car_id = item["specid"]
            if key_car_id != None and len(str(key_car_id)) != 0:
                car_id = int(key_car_id)
                car = NewAutoHomeCar(car_id)
                ret[car_id] = car

    # 基本参数抓取
    result = demjson.decode(str_base)["result"]["paramtypeitems"]
    if type(result) != None and len(result) != 0:
        items = list(result)
        for item in items:
            item_name = str(item["name"])

            if item_name == "基本参数":
                base_params = list(item["paramitems"])

                for v in base_params:
                    name = str(v["name"])
                    # 能源类型
                    if name.count("能源类型") > 0:
                        GraspTheData(v, "valueitems", ret, "energy_type_str", dic)
                    # 上市时间
                    if name.count("上市") > 0:
                        GraspTheData(v, "valueitems", ret, "market_time", dic)
                    # 工信部纯电续航里程
                    if name.count(("工信部纯电续航里程")) > 0:
                        GraspTheData(v, "valueitems", ret, "e_mileage", dic)
                    # 变速箱
                    if name.count(("变速箱")) > 0:
                        GraspTheData(v, "valueitems", ret, "gearbox", dic)

                    id = int(v["id"])
                    # 级别
                    if id == 220:
                        GraspTheData(v, "valueitems", ret, "car_level_str", dic)
                    # 车型名称
                    elif id == 567:
                        GraspTheData(v, "valueitems", ret, "car_name", dic)
                    # 最大功率
                    elif id == 295:
                        GraspTheData(v, "valueitems", ret, "max_power", dic)
                    # 最大扭矩
                    elif id == 571:
                        GraspTheData(v, "valueitems", ret, "max_torque", dic)
                    # 发动机
                    elif id == 555:
                        GraspTheData(v, "valueitems", ret, "engine", dic)
                    # 长*宽*高
                    elif id == 222:
                        GraspTheData(v, "valueitems", ret, "car_size", dic)
                    # 车身结构
                    elif id == 281:
                        GraspTheData(v, "valueitems", ret, "car_struct", dic)
                    # 最高车速
                    elif id == 267:
                        GraspTheData(v, "valueitems", ret, "max_speed", dic)
                    # 官方100加速
                    elif id == 225:
                        GraspTheData(v, "valueitems", ret, "official_speedup", dic)
                    # 实测100加速
                    elif id == 272:
                        GraspTheData(v, "valueitems", ret, "actual_speedup", dic)
                    # 实测100制动
                    elif id == 273:
                        GraspTheData(v, "valueitems", ret, "actual_brake", dic)
                    # 工信部综合油耗
                    elif id == 271:
                        GraspTheData(v, "valueitems", ret, "gerenal_fueluse", dic)
                    # 实测油耗
                    elif id == 243:
                        GraspTheData(v, "valueitems", ret, "actual_fueluse", dic)
                    # 整车质保
                    elif id == 274:
                        GraspTheData(v, "valueitems", ret, "quality_guarantee", dic)
                    else:
                        pass

            if item_name == "车身":
                body_params = list(item["paramitems"])

                for v in body_params:
                    id = int(v["id"])

                    # 长度(mm)
                    if id == 275:
                        GraspTheData(v, "valueitems", ret, "length", dic)
                    # 宽度(mm)
                    elif id == 276:
                        GraspTheData(v, "valueitems", ret, "width", dic)
                    # 高度(mm)
                    elif id == 277:
                        GraspTheData(v, "valueitems", ret, "height", dic)
                    # 轴距(mm)
                    elif id == 132:
                        GraspTheData(v, "valueitems", ret, "shaft_distance", dic)
                    # 前轮距(mm)
                    elif id == 278:
                        GraspTheData(v, "valueitems", ret, "front_wheels_gap", dic)
                    # 后轮距(mm)
                    elif id == 638:
                        GraspTheData(v, "valueitems", ret, "back_wheels_gap", dic)
                    # 最小离地间隙(mm)
                    elif id == 279:
                        GraspTheData(v, "valueitems", ret, "min_ground", dic)
                    # 整备质量(kg)
                    elif id == 280:
                        GraspTheData(v, "valueitems", ret, "total_weight", dic)
                    # 车身结构
                    elif id == 281:
                        GraspTheData(v, "valueitems", ret, "body_struct", dic)
                    # 车门数
                    elif id == 282:
                        GraspTheData(v, "valueitems", ret, "doors", dic)
                    # 座位数
                    elif id == 283:
                        GraspTheData(v, "valueitems", ret, "seats", dic)
                    # 油箱容积(L)
                    elif id == 284:
                        GraspTheData(v, "valueitems", ret, "fuel_vol", dic)
                    # 行李厢容积(L)
                    elif id == 285:
                        GraspTheData(v, "valueitems", ret, "cargo_vol", dic)
                    else:
                        pass

            if item_name == "发动机":
                engine_params = list(item["paramitems"])

                for v in engine_params:
                    id = int(v["id"])

                    # 发动机型号
                    if id == 570:
                        GraspTheData(v, "valueitems", ret, "engine_type", dic)
                    # 排量(mL)
                    elif id == 287:
                        GraspTheData(v, "valueitems", ret, "cc", dic)
                    # 进气形式
                    elif id == 640:
                        GraspTheData(v, "valueitems", ret, "air_intake", dic)
                    # 气缸排列形式
                    elif id == 289:
                        GraspTheData(v, "valueitems", ret, "cylinder_arrange", dic)
                    # 气缸个数
                    elif id == 290:
                        GraspTheData(v, "valueitems", ret, "cylinders", dic)
                    # 每缸气门数
                    elif id == 291:
                        GraspTheData(v, "valueitems", ret, "valves", dic)
                    # 压缩比
                    elif id == 182:
                        GraspTheData(v, "valueitems", ret, "compress_rate", dic)
                    # 配气机构
                    elif id == 641:
                        GraspTheData(v, "valueitems", ret, "valve_machanism", dic)
                    # 缸径(mm)
                    elif id == 181:
                        GraspTheData(v, "valueitems", ret, "cylinder_radius", dic)
                    # 行程(mm)
                    elif id == 293:
                        GraspTheData(v, "valueitems", ret, "stroke", dic)
                    # 最大马力(Ps)
                    elif id == 294:
                        GraspTheData(v, "valueitems", ret, "engine_hp", dic)
                    # 最大功率(kW)
                    elif id == 295:
                        GraspTheData(v, "valueitems", ret, "engine_power", dic)
                    # 最大功率转速(rpm)
                    elif id == 296:
                        GraspTheData(v, "valueitems", ret, "engine_rpm", dic)
                    # 最大扭矩(N·m)
                    elif id == 571:
                        GraspTheData(v, "valueitems", ret, "engine_torque", dic)
                    # 最大扭矩转速(rpm)
                    elif id == 642:
                        GraspTheData(v, "valueitems", ret, "torque_rpm", dic)
                    # 发动机特有技术
                    elif id == 642:
                        GraspTheData(v, "valueitems", ret, "tech_spec", dic)
                    # 燃料形式
                    elif id == 572:
                        GraspTheData(v, "valueitems", ret, "engine_energy", dic)
                    # 燃油标号
                    elif id == 573:
                        GraspTheData(v, "valueitems", ret, "roz", dic)
                    # 供油方式
                    elif id == 574:
                        GraspTheData(v, "valueitems", ret, "oil_drive", dic)
                    # 缸盖材料
                    elif id == 575:
                        GraspTheData(v, "valueitems", ret, "cylinder_cover", dic)
                    # 缸体材料
                    elif id == 576:
                        GraspTheData(v, "valueitems", ret, "cylinder_body", dic)
                    # 环保标准
                    elif id == 577:
                        GraspTheData(v, "valueitems", ret, "environmental_standard", dic)
                    else:
                        pass

            if item_name == "电动机":
                motor_params = list(item["paramitems"])

                for v in motor_params:
                    name = str(v["name"])
                    if name == "电机类型":
                        GraspTheData(v, "valueitems", ret, "motor_type", dic)
                        GraspTheData(v, "valueitems", ret, "car_type", dic)

                    if name == "驱动电机数":
                        GraspTheData(v, "valueitems", ret, "motor_num", dic)

                    if name == "电机布局":
                        GraspTheData(v, "valueitems", ret, "motor_arrange", dic)

                    id = int(v["id"])

                    # 电动机总功率
                    if id == 1325:
                        GraspTheData(v, "valueitems", ret, "motor_power", dic)
                    # 电动机总扭矩
                    elif id == 1326:
                        GraspTheData(v, "valueitems", ret, "engine_type", dic)
                    # 前电动机最大功率
                    elif id == 1327:
                        GraspTheData(v, "valueitems", ret, "motor_front_power", dic)
                    # 前电动机最大扭矩
                    elif id == 1328:
                        GraspTheData(v, "valueitems", ret, "motor_front_torque", dic)
                    # 后电动机最大功率
                    elif id == 1329:
                        GraspTheData(v, "valueitems", ret, "motor_back_power", dic)
                    # 后电动机最大扭矩
                    elif id == 1330:
                        GraspTheData(v, "valueitems", ret, "motor_back_torque", dic)
                    # 工信部续航里程
                    elif id == 1013:
                        GraspTheData(v, "valueitems", ret, "mileage", dic)
                    # 电池容量
                    elif id == 1124:
                        GraspTheData(v, "valueitems", ret, "bat_cap", dic)
                    else:
                        pass

            if item_name == "变速箱":
                gearboxes = list(item["paramitems"])

                for v in gearboxes:
                    id = int(v["id"])

                    # 挡位个数
                    if id == 559:
                        GraspTheData(v, "valueitems", ret, "gears_num", dic)
                    # 变速箱类型
                    elif id == 221:
                        GraspTheData(v, "valueitems", ret, "gears_type", dic)
                    # 简称
                    elif id == 1072:
                        GraspTheData(v, "valueitems", ret, "gearbox_name", dic)
                    else:
                        pass

            if item_name == "底盘转向":
                underpan = list(item["paramitems"])

                for v in underpan:
                    id = int(v["id"])

                    # 驱动方式
                    if id == 395:
                        GraspTheData(v, "valueitems", ret, "drive_method", dic)
                    # 前悬架类型
                    elif id == 578:
                        GraspTheData(v, "valueitems", ret, "susp_front_type", dic)
                    # 后悬架类型
                    elif id == 579:
                        GraspTheData(v, "valueitems", ret, "susp_back_type", dic)
                    # 助力类型
                    elif id == 510:
                        GraspTheData(v, "valueitems", ret, "assist_type", dic)
                    # 车体结构
                    elif id == 223:
                        GraspTheData(v, "valueitems", ret, "structure", dic)
                    # 四驱形式
                    elif id == 412:
                        GraspTheData(v, "valueitems", ret, "four_wheel_drive", dic)
                    # 中央差速器结构
                    elif id == 415:
                        GraspTheData(v, "valueitems", ret, "central_diff", dic)
                    else:
                        pass

            if item_name == "车轮制动":
                brake_params = list(item["paramitems"])

                for v in brake_params:
                    id = int(v["id"])

                    # 前制动器类型
                    if id == 511:
                        GraspTheData(v, "valueitems", ret, "front_brake", dic)
                    # 后制动器类型
                    elif id == 512:
                        GraspTheData(v, "valueitems", ret, "back_brake", dic)
                    # 驻车制动类型
                    elif id == 513:
                        GraspTheData(v, "valueitems", ret, "park_brake", dic)
                    # 前轮胎规格
                    elif id == 580:
                        GraspTheData(v, "valueitems", ret, "front_wheel_size", dic)
                    # 后轮胎规格
                    elif id == 581:
                        GraspTheData(v, "valueitems", ret, "back_wheel_size", dic)
                    # 备胎规格
                    elif id == 515:
                        GraspTheData(v, "valueitems", ret, "backup_wheel", dic)
                    else:
                        pass

    # 可选参数抓取
    result = demjson.decode(str_option)["result"]["configtypeitems"]
    if type(result) != None and len(result) != 0:
        items = list(result)

        for item in items:
            item_name = str(item["name"])

            if item_name == "主/被动安全装备":
                if isinstance(item["configitems"], list):
                    secure_params = list(item["configitems"])

                    # 疲劳驾驶提示id为0
                    for v in secure_params:
                        id = int(v["id"])

                        # 主/副驾驶座安全气囊
                        if id == 1082:
                            GraspTheData(v, "valueitems", ret, "seat_srs", dic)
                        # 前/后排侧气囊
                        elif id == 421:
                            GraspTheData(v, "valueitems", ret, "side_airbag", dic)
                        # 前/后排头部气囊(气帘)
                        elif id == 422:
                            GraspTheData(v, "valueitems", ret, "head_srs", dic)
                        # 膝部气囊
                        elif id == 423:
                            GraspTheData(v, "valueitems", ret, "knee_srs", dic)
                        # 胎压监测装置
                        elif id == 551:
                            GraspTheData(v, "valueitems", ret, "tire_pres_monitor", dic)
                        # 零胎压继续行驶
                        elif id == 424:
                            GraspTheData(v, "valueitems", ret, "zero_tire_pres", dic)
                        # 安全带未系提示
                        elif id == 552:
                            GraspTheData(v, "valueitems", ret, "unbelt_notice", dic)
                        # ISOFIX儿童座椅接口
                        elif id == 1084:
                            GraspTheData(v, "valueitems", ret, "isofix", dic)
                        # ABS防抱死
                        elif id == 110:
                            GraspTheData(v, "valueitems", ret, "anti_lock", dic)
                        # 刹车辅助(EBA/BAS/BA等)
                        elif id == 437:
                            GraspTheData(v, "valueitems", ret, "bas", dic)
                        # 牵引力控制(ASR/TCS/TRC等)
                        elif id == 438:
                            GraspTheData(v, "valueitems", ret, "tcs", dic)
                        # 车身稳定控制(ESC/ESP/DSC等)
                        elif id == 109:
                            GraspTheData(v, "valueitems", ret, "stable_control", dic)
                        # 并线辅助
                        elif id == 426:
                            GraspTheData(v, "valueitems", ret, "bsa", dic)
                        # 车道偏离预警系统
                        elif id == 788:
                            GraspTheData(v, "valueitems", ret, "ldw", dic)
                        # 主动刹车/主动安全系统
                        elif id == 436:
                            GraspTheData(v, "valueitems", ret, "abs", dic)
                        # 夜视系统
                        elif id == 637:
                            GraspTheData(v, "valueitems", ret, "nvs", dic)
                        else:
                            pass

            if item_name == "辅助/操控配置":
                if isinstance(item["configitems"], list):
                    oper_params = list(item["configitems"])

                    for v in oper_params:
                        name = str(v["name"])

                        if name == "上坡辅助":
                            GraspTheData(v, "valueitems", ret, "hac", dic)

                        id = int(v["id"])

                        # 前/后驻车雷达
                        if id == 1086:
                            GraspTheData(v, "valueitems", ret, "radar", dic)
                        # 倒车视频影像
                        elif id == 448:
                            GraspTheData(v, "valueitems", ret, "reverse_video", dic)
                        # 全景摄像头
                        elif id == 473:
                            GraspTheData(v, "valueitems", ret, "panorama", dic)
                        # 定速巡航
                        elif id == 445:
                            GraspTheData(v, "valueitems", ret, "cruise_ctrl", dic)
                        # 自适应巡航
                        elif id == 446:
                            GraspTheData(v, "valueitems", ret, "self_adpt_cruise", dic)
                        # 自动泊车入位
                        elif id == 472:
                            GraspTheData(v, "valueitems", ret, "auto_park_in", dic)
                        # 发动机启停技术
                        elif id == 334:
                            GraspTheData(v, "valueitems", ret, "engine_start_stop", dic)
                        # 自动驻车
                        elif id == 363:
                            GraspTheData(v, "valueitems", ret, "auto_park", dic)
                        # 陡坡缓降
                        elif id == 138:
                            GraspTheData(v, "valueitems", ret, "hdc", dic)
                        # 可变悬架
                        elif id == 399:
                            GraspTheData(v, "valueitems", ret, "variable_susp", dic)
                        # 空气悬架
                        elif id == 167:
                            GraspTheData(v, "valueitems", ret, "air_susp", dic)
                        # 可变转向比
                        elif id == 409:
                            GraspTheData(v, "valueitems", ret, "vgrs", dic)
                        # 前桥限滑差速器/差速锁
                        elif id == 975:
                            GraspTheData(v, "valueitems", ret, "front_diff_lock", dic)
                        # 中央差速器锁止功能
                        elif id == 976:
                            GraspTheData(v, "valueitems", ret, "central_diff_lock", dic)
                        # 后桥限滑差速器/差速锁
                        elif id == 977:
                            GraspTheData(v, "valueitems", ret, "back_diff_lock", dic)
                        # 整体主动转向系统
                        elif id == 404:
                            GraspTheData(v, "valueitems", ret, "ads", dic)
                        else:
                            pass

            if item_name == "外部/防盗配置":
                if isinstance(item["configitems"], list):
                    guard_params = list(item["configitems"])

                    for v in guard_params:
                        name = str(v["name"])

                        if name == "远程启动":
                            GraspTheData(v, "valueitems", ret, "remote_start", dic)

                        if name == "车顶行李架":
                            GraspTheData(v, "valueitems", ret, "roof_rack", dic)

                        if name == "感应后备厢":
                            GraspTheData(v, "valueitems", ret, "react_cargo", dic)

                        id = int(v["id"])

                        # 电动天窗
                        if id == 583:
                            GraspTheData(v, "valueitems", ret, "e_sunroof", dic)
                        # 全景天窗
                        elif id == 584:
                            GraspTheData(v, "valueitems", ret, "pano_sunroof", dic)
                        # 运动外观套件
                        elif id == 585:
                            GraspTheData(v, "valueitems", ret, "pano_sunroof", dic)
                        # 铝合金轮圈
                        elif id == 525:
                            GraspTheData(v, "valueitems", ret, "alloy_wheel", dic)
                        # 电动吸合门
                        elif id == 443:
                            GraspTheData(v, "valueitems", ret, "e_suction_door", dic)
                        # 侧滑门
                        elif id == 1122:
                            GraspTheData(v, "valueitems", ret, "slide_door", dic)
                        # 电动后备厢
                        elif id == 452:
                            GraspTheData(v, "valueitems", ret, "e_cargo", dic)
                        # 发动机电子防盗
                        elif id == 481:
                            GraspTheData(v, "valueitems", ret, "engine_e_guard", dic)
                        # 车内中控锁
                        elif id == 558:
                            GraspTheData(v, "valueitems", ret, "e_ctrl_lock", dic)
                        # 遥控钥匙
                        elif id == 582:
                            GraspTheData(v, "valueitems", ret, "remote_key", dic)
                        # 无钥匙启动系统
                        elif id == 431:
                            GraspTheData(v, "valueitems", ret, "keyless_start", dic)
                        # 无钥匙进入系统
                        elif id == 1066:
                            GraspTheData(v, "valueitems", ret, "keyless_enter", dic)
                        else:
                            pass

            if item_name == "内部配置":
                if isinstance(item["configitems"], list):
                    inside_params = list(item["configitems"])

                    for v in inside_params:
                        name = str(v["name"])

                        if name == "皮质方向盘":
                            GraspTheData(v, "valueitems", ret, "leather_steering", dic)

                        if name == "方向盘记忆":
                            GraspTheData(v, "valueitems", ret, "steer_mem", dic)

                        if name == "内置行车记录仪":
                            GraspTheData(v, "valueitems", ret, "car_dvr", dic)

                        if name.count("降噪") > 0:
                            GraspTheData(v, "valueitems", ret, "anc", dic)

                        if name.count("手机无线") > 0:
                            GraspTheData(v, "valueitems", ret, "wireless_charge", dic)

                        id = int(v["id"])

                        # 方向盘调节
                        if id == 1085:
                            GraspTheData(v, "valueitems", ret, "steer_adjt", dic)
                        # 方向盘电动调节
                        elif id == 589:
                            GraspTheData(v, "valueitems", ret, "steer_e_adjt", dic)
                        # 多功能方向盘
                        elif id == 444:
                            GraspTheData(v, "valueitems", ret, "functional_steer", dic)
                        # 方向盘换挡
                        elif id == 468:
                            GraspTheData(v, "valueitems", ret, "steer_shift", dic)
                        # 方向盘加热
                        elif id == 1064:
                            GraspTheData(v, "valueitems", ret, "steer_heat", dic)
                        # 行车电脑显示屏
                        elif id == 590:
                            GraspTheData(v, "valueitems", ret, "computer_scr", dic)
                        # HUD抬头数字显示
                        elif id == 471:
                            GraspTheData(v, "valueitems", ret, "hud", dic)
                        else:
                            pass

            if item_name == "座椅配置":
                if isinstance(item["configitems"], list):
                    seat_params = list(item["configitems"])
                    # 无法抓取：副驾驶位后排可调节按钮、第二排独立座椅、可加热/制冷杯架
                    for i, v in enumerate(seat_params):
                        id = int(v["id"])

                        # 座椅材质
                        if i == 0:
                            GraspTheData(v, "valueitems", ret, "seat_mat", dic)

                        # 运动风格座椅
                        if id == 592:
                            GraspTheData(v, "valueitems", ret, "sport_seat", dic)
                        # 座椅高低调节
                        elif id == 639:
                            GraspTheData(v, "valueitems", ret, "height_adjt", dic)
                        # 腰部支撑调节
                        elif id == 449:
                            GraspTheData(v, "valueitems", ret, "lumbar_support", dic)
                        # 肩部支撑调节
                        elif id == 593:
                            GraspTheData(v, "valueitems", ret, "shoulder_support", dic)
                        # 主/副驾驶座电动调节
                        elif id == 1087:
                            GraspTheData(v, "valueitems", ret, "seat_e_adjt", dic)
                        # 第二排靠背角度调节
                        elif id == 595:
                            GraspTheData(v, "valueitems", ret, "snd_backrest_adjt", dic)
                        # 第二排座椅移动
                        elif id == 596:
                            GraspTheData(v, "valueitems", ret, "snd_seat_mv", dic)
                        # 后排座椅电动调节
                        elif id == 597:
                            GraspTheData(v, "valueitems", ret, "back_seat_adjt", dic)
                        # 电动座椅记忆
                        elif id == 598:
                            GraspTheData(v, "valueitems", ret, "e_seat_mem", dic)
                        # 前/后排座椅加热
                        elif id == 1088:
                            GraspTheData(v, "valueitems", ret, "seat_heat", dic)
                        # 前/后排座椅通风
                        elif id == 1089:
                            GraspTheData(v, "valueitems", ret, "seat_vent", dic)
                        # 前/后排座椅按摩
                        elif id == 1090:
                            GraspTheData(v, "valueitems", ret, "seat_masg", dic)
                        # 第三排座椅
                        elif id == 603:
                            GraspTheData(v, "valueitems", ret, "third_row_seat", dic)
                        # 后排座椅放倒方式
                        elif id == 1091:
                            GraspTheData(v, "valueitems", ret, "back_seat_down", dic)
                        # 前/后中央扶手
                        elif id == 1092:
                            GraspTheData(v, "valueitems", ret, "handrail", dic)
                        # 后排杯架
                        elif id == 606:
                            GraspTheData(v, "valueitems", ret, "back_cup_hold", dic)
                        else:
                            pass

            if item_name == "多媒体配置":
                if isinstance(item["configitems"], list):
                    media_params = list(item["configitems"])
                    # 无法抓取外接音源接口
                    for v in media_params:
                        name = str(v["name"])
                        if name == "中控台彩色大屏尺寸":
                            GraspTheData(v, "valueitems", ret, "colorful_scr_size", dic)

                        if name == "手机互联/映射":
                            GraspTheData(v, "valueitems", ret, "mobile_map", dic)

                        if name == "车联网":
                            GraspTheData(v, "valueitems", ret, "network", dic)

                        if name == "220V/230V电源":
                            GraspTheData(v, "valueitems", ret, "back_power_supply", dic)

                        if name == "CD/DVD":
                            GraspTheData(v, "valueitems", ret, "cddvd", dic)

                        id = int(v["id"])

                        # GPS导航系统
                        if id == 607:
                            GraspTheData(v, "valueitems", ret, "gps", dic)
                        # 定位互动服务
                        elif id == 455:
                            GraspTheData(v, "valueitems", ret, "gps_interact", dic)
                        # 中控台彩色大屏
                        elif id == 608:
                            GraspTheData(v, "valueitems", ret, "colorful_scr", dic)
                        # 中控液晶屏分屏显示
                        elif id == 464:
                            GraspTheData(v, "valueitems", ret, "lcd_sep", dic)
                        # 蓝牙/车载电话
                        elif id == 609:
                            GraspTheData(v, "valueitems", ret, "blueteeth", dic)
                        # 车载电视
                        elif id == 610:
                            GraspTheData(v, "valueitems", ret, "television", dic)
                        # 后排液晶屏
                        elif id == 611:
                            GraspTheData(v, "valueitems", ret, "back_lcd", dic)
                        # 扬声器品牌
                        elif id == 1212:
                            GraspTheData(v, "valueitems", ret, "speaker_brand", dic)
                        # 扬声器数量
                        elif id == 618:
                            GraspTheData(v, "valueitems", ret, "speaker_num", dic)
                        else:
                            pass

            if item_name == "灯光配置":
                if isinstance(item["configitems"], list):
                    light_params = list(item["configitems"])

                    for i, v in enumerate(light_params):
                        # 近光灯
                        if i == 0:
                            GraspTheData(v, "valueitems", ret, "low_beam", dic)

                        # 远光灯
                        if i == 1:
                            GraspTheData(v, "valueitems", ret, "high_beam", dic)

                        name = str(v["name"])
                        if name == "LED日间行车灯":
                            GraspTheData(v, "valueitems", ret, "led_beam", dic)

                        if name == "转向头灯":
                            GraspTheData(v, "valueitems", ret, "turn_head_light", dic)

                        if name.count("应远近光") > 0:
                            GraspTheData(v, "valueitems", ret, "adaptive_beam", dic)

                        id = int(v["id"])

                        # 自动头灯
                        if id == 441:
                            GraspTheData(v, "valueitems", ret, "head_light", dic)
                        # 转向辅助灯
                        elif id == 1161:
                            GraspTheData(v, "valueitems", ret, "turn_light", dic)
                        # 前雾灯
                        elif id == 619:
                            GraspTheData(v, "valueitems", ret, "front_fog_lamp", dic)
                        # 大灯高度可调
                        elif id == 620:
                            GraspTheData(v, "valueitems", ret, "light_height_adjt", dic)
                        # 大灯清洗装置
                        elif id == 621:
                            GraspTheData(v, "valueitems", ret, "light_clean_dev", dic)
                        # 车内氛围灯
                        elif id == 453:
                            GraspTheData(v, "valueitems", ret, "mood_light", dic)
                        else:
                            pass

            if item_name == "玻璃/后视镜":
                if isinstance(item["configitems"], list):
                    glass_params = list(item["configitems"])

                    for v in glass_params:
                        name = str(v["name"])
                        if name.count("车窗一键") > 0:
                            GraspTheData(v, "valueitems", ret, "e_lift_window", dic)

                        if name == "流媒体车内后视镜":
                            GraspTheData(v, "valueitems", ret, "stream_media_rearview", dic)

                        id = int(v["id"])

                        # 前/后电动车窗
                        if id == 622:
                            GraspTheData(v, "valueitems", ret, "power_window", dic)
                        # 车窗防夹手功能
                        elif id == 623:
                            GraspTheData(v, "valueitems", ret, "anti_pinch_hand", dic)
                        # 防紫外线/隔热玻璃
                        elif id == 624:
                            GraspTheData(v, "valueitems", ret, "insulating_glass", dic)
                        # 后视镜电动调节
                        elif id == 625:
                            GraspTheData(v, "valueitems", ret, "e_adjt_rearview", dic)
                        # 后视镜加热
                        elif id == 626:
                            GraspTheData(v, "valueitems", ret, "heat_rearview", dic)
                        # 内/外后视镜自动防眩目
                        elif id == 1095:
                            GraspTheData(v, "valueitems", ret, "dimming_mirror", dic)
                        # 后视镜电动折叠
                        elif id == 628:
                            GraspTheData(v, "valueitems", ret, "power_mirror", dic)
                        # 后视镜记忆
                        elif id == 629:
                            GraspTheData(v, "valueitems", ret, "mirror_mem", dic)
                        # 后风挡遮阳帘
                        elif id == 630:
                            GraspTheData(v, "valueitems", ret, "abat_vent", dic)
                        # 后排侧遮阳帘
                        elif id == 631:
                            GraspTheData(v, "valueitems", ret, "side_abat_vent", dic)
                        # 后排侧隐私玻璃
                        elif id == 1063:
                            GraspTheData(v, "valueitems", ret, "side_priv_glass", dic)
                        # 遮阳板化妆镜
                        elif id == 632:
                            GraspTheData(v, "valueitems", ret, "sun_shield", dic)
                        # 后雨刷
                        elif id == 633:
                            GraspTheData(v, "valueitems", ret, "back_wiper", dic)
                        # 感应雨刷
                        elif id == 454:
                            GraspTheData(v, "valueitems", ret, "react_wiper", dic)
                        else:
                            pass

            if item_name == "空调/冰箱":
                if isinstance(item["configitems"], list):
                    air_params = list(item["configitems"])

                    for v in air_params:
                        name = str(v["name"])
                        if name.count("净化器") > 0:
                            GraspTheData(v, "valueitems", ret, "air_cleaner", dic)

                        id = int(v["id"])

                        # 空调控制方式
                        if id == 1097:
                            GraspTheData(v, "valueitems", ret, "air_type", dic)
                        # 后排独立空调
                        elif id == 459:
                            GraspTheData(v, "valueitems", ret, "back_air", dic)
                        # 后座出风口
                        elif id == 634:
                            GraspTheData(v, "valueitems", ret, "back_outlet", dic)
                        # 温度分区控制
                        elif id == 463:
                            GraspTheData(v, "valueitems", ret, "temper_zone_ctrl", dic)
                        # 车内空气调节/花粉过滤
                        elif id == 635:
                            GraspTheData(v, "valueitems", ret, "air_adjt", dic)
                        # 车载冰箱
                        elif id == 636:
                            GraspTheData(v, "valueitems", ret, "car_fridge", dic)
                        else:
                            pass

    return ret


def decodeJsFuncs(string):
    try:
        pos = string.index("var")
    except ValueError:
        pos = -1
    if pos > 0:
        string = string[:pos]
    key = string.split("()")[0]
    key = key.replace('function', '')
    key = key.strip()
    if string.endswith('function'):
        string = string.rstrip('function')
    string = string.strip()
    if len(re.compile(r'function').findall(string)) > 1:
        try:
            function_name = re.search(r'''
                    function\s+(\w+)\(\)\s*\{\s*
                        function\s+\w+\(\)\s*\{\s*
                            return\s+[\'\"]([^\'\"]+)[\'\"];\s*
                        \};\s*
                        if\s*\(\w+\(\)\s*==\s*[\'\"]([^\'\"]+)[\'\"]\)\s*\{\s*
                            return\s*[\'\"]([^\'\"]+)[\'\"];\s*
                        \}\s*else\s*\{\s*
                            return\s*\w+\(\);\s*
                        \}\s*
                    \}
                    ''', string, re.X)
            a, b, c, d = function_name.groups()
            value = d if b == c else b
            return key, value
        except:
            function_name = re.search(r'''
                    function\s+(\w+)\(\)\s*\{\s*
                        function\s+\w+\(\)\s*\{\s*
                            return\s+[\'\"]([^\'\"]+)[\'\"];\s*
                        \};\s*
                        if\s*\(\w+\(\)\s*==\s*[\'\"]([^\'\"]+)[\'\"]\)\s*\{\s*
                            return\s*\w+\(\);\s*
                        \}\s*else\s*\{\s*
                            return\s*[\'\"]([^\'\"]+)[\'\"];\s*
                        \}\s*
                    \}
                    ''', string, re.X)
            a, b, c, d = function_name.groups()
            value = b if b == c else d
            return key, value
    else:
        function_name = re.search(r'''
            function\s*(\w+)\(\)\s*\{\s*
                [\'\"]return\s*[^\'\"]+[\'\"];\s*
                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
            \}\s*
        ''', string, re.X)
        a, b = function_name.groups()
        value = b
        return key, value


def decodeJsVars(string):
    string = string.replace('var', '')
    string = string.strip()
    if string.count("=") > 0:
        pair = string.split("=", 2)
        key = pair[0].strip()
        value = pair[1].strip()
        value = value.strip("'")
        return key, value


def decodeJsVarfuncs(string):
    string = string.replace("var", "")
    string = string.strip()
    if string.count("=") > 0:
        pair = string.split("=", 2)
        key = pair[0]
        if pair[1].count("function") > 0:
            if len(re.compile(r'function').findall(string)) > 1:
                function_name = re.search(r'''
                            [A-z]{0,2}_=function\(\)\{\'\S{0,2}_\';\s*
                                \s_\w=function\(\)\{return\s*[\'\"]([^\'\"]+)[\'\"];\};\s*
                                return\s*_[A-z]\(\);\}\s*
                            ''', string, re.X)
                a = function_name.group(1)
                value = a
                return key, value
            else:
                function_name = re.search(r'''
                             [A-z]{0,2}_=function\(\)\s*\{\s*
                                [\'\"]return\s*[A-z]{0,2}_+[\'\"];\s*
                                return\s*[\'\"]([^\'\"]+)[\'\"];\s*
                                \}\s*
                        ''', string, re.X)
                a = function_name.group(1)
                value = a
                return key, value


def replaceDashAsNullString(s):
    if s.count("&nbsp;") > 0:
        s = s.replace("&nbsp;", "")
    return s


def getAutoHomeDict(js):
    map_strs = {}
    dict_slice = {}
    map_source = {}
    dic = ""
    string = js.replace("})(document);</script>", "function")
    matches = re.compile(r"function\s\S\S_\(\)\s*\{.*?\}+\s+").findall(js)                                  # 匹配function
    for fc in matches:
        key, value = decodeJsFuncs(fc)
        map_source[key] = fc
        if key != '':
            map_strs[key] = value
    matches = re.compile(r"var\s?\S\S_=\s?'\S*'").findall(string)                                           # 匹配var申明
    for variable in matches:
        key, value = decodeJsVars(variable)
        map_source[key] = variable
        if key != '':
            map_strs[key] = value
    matches = re.compile(r"var\s?\S\S_=\s?function\s?\(\)\s?\{.*?return.*?return.*?\}").findall(string)      # 匹配var和functions
    for varfunc in matches:
        key, value = decodeJsVarfuncs(varfunc)
        map_source[key] = varfunc
        if key != "":
            map_strs[key] = value
    pattren = re.compile(r"function\s*\$FillDicData\$\s*\(\)\s*?{.*?\$RenderToHTML")                         # 拼接字典
    is_match = pattren.search(js)
    if is_match != None:
        str_match = str(pattren.findall(js))

        if str_match.find("$GetWindow$()") == -1:
            pass
        position = str_match.index("$GetWindow$()")
        str_tmp = str_match[position:]

        if str_match.find("$rulePosList$") == -1:
            pass
        position = str_match.index("$rulePosList$")
        str_tmp = str_match[:position]

        if str_match.find("]") == -1:
            pass
        position = str_match.index("]")
        str_tmp = str_tmp[position + 1:]
        strs_dict = str_tmp.split("+")

        i = 1
        while i < len(strs_dict):
            str_to_match = strs_dict[i]
            is_match = re.compile(r"\(\'\S+\'\)").search(str_to_match)

            if is_match != None:
                tmp = re.compile(r"\(\'\S+\'\)").findall(str_to_match)[0]
                tmp = tmp.replace("(", "")
                tmp = tmp.replace(")", "")
                tmp = tmp.replace("'", "")
                tmp = tmp.strip()
                dic += tmp

            elif re.compile(r"^\'\S+\'$").search(str_to_match) != None:
                tmp = str_to_match.replace("'", "")
                tmp = tmp.strip()
                dic += tmp

            elif re.compile(r"\(function\s{0,3}\(\)\{.*?return.*?return.*?\}\)").search(str_to_match) != None:
                str_matched = re.compile(r"\(function\s{0,3}\(\)\{.*?return.*?return.*?\}\)").match(str_to_match)

                if re.compile(r"return\s?\'\S+\'").search(str(str_matched)) != None:
                    str_tmp = re.compile(r"return\s?\'\S+\'").findall(str(str_matched))[0]

                    tmp = str_tmp.replace("return", "")
                    tmp = tmp.replace("'", "")
                    tmp = tmp.strip()
                    dic += tmp

            elif re.compile(r"^\S{2}_\(\)$").search(str_to_match) != None:
                key = str_to_match.replace("()", "")
                tmp = map_strs[key]
                dic += tmp

            elif re.compile(r"^\S{2}_$").search(str_to_match) != None:
                key = str_to_match
                dic += map_strs[key]

            elif re.compile(r"\('([A-Z]|[a-z]|[0-9]|[,]|[']|[;]|[\u4e00-\u9fbb]){1,10}'\)").search(str_to_match) != None:
                tmp = re.compile(r"\('([A-Z]|[a-z]|[0-9]|[,]|[']|[;]|[\u4e00-\u9fbb]){1,10}'\)").match(str_to_match)
                if len(tmp) >= 2:
                    tmp = tmp[:2]
                dic += tmp

            else:
                dic += "X"

            i += 1

    indexes = ""                                                                                             # 拼接字符串
    position = str_match.find("$rulePosList$")
    str_tmp = str_match[position:]

    position = str_tmp.find("$SystemFunction2$")
    str_tmp = str_tmp[:position - 2]
    str_tmp = str_tmp.strip()
    strs_indexes = str_tmp.split("+")
    i = 1
    while i < len(strs_indexes):
        str_to_match = strs_indexes[i]
        tmp = ""

        if re.compile(r"\(\'\S+\'\)").search(str(str_to_match)) != None:
            tmp = re.compile(r"\(\'\S+\'\)").findall(str_to_match)
            tmp = str(tmp).replace("(", "")
            tmp = tmp.replace(")", "")
            tmp = tmp.replace("'", "")
            tmp = tmp.strip()
            tmp = tmp.strip("[")
            tmp = tmp.strip("]")
            tmp = tmp.strip('"')
            indexes += tmp

        elif re.compile(r"^\'\S+\'$").search(str(str_to_match)) != None:
            tmp = str_to_match.replace("'", "")
            tmp = tmp.strip()
            indexes += tmp

        elif re.compile(r"\(function\s{0,3}\(\)\{.*?return.*?return.*?\}\)").search(str(str_to_match)) != None:
            str_matched = re.compile(r"\(function\s{0,3}\(\)\{.*?return.*?return.*?\}\)").findall(str_to_match)

            if re.compile(r"return\s?\'\S+\'").search(str(str_to_match)) != None:
                str_tmp = re.compile(r"return\s?\'\S+\'").findall(str(str_matched))

                tmp = str(str_tmp).replace("return", "")
                tmp = tmp.replace("'", "")
                tmp = tmp.strip()
                tmp = tmp.strip("[")
                tmp = tmp.strip("]")
                tmp = tmp.strip('"')
                indexes += tmp

        elif re.compile(r"^\S{2}_\(\)$").search(str(str_to_match)) != None:
            key = str_to_match.replace("()", "")
            tmp = map_strs[key]
            indexes += tmp

        elif re.compile(r"^\S{2}_$").search(str(str_to_match)) != None:
            key = str_to_match
            tmp = map_strs[key]
            indexes += tmp

        elif str_to_match.strip() == "''":
            i += 1
            continue

        else:
            indexes += "X"

        i += 1

    runes_dic = []
    for d in dic:
        d = ord(d)
        runes_dic.append(d)
    items = indexes.split(";")
    for i, string in enumerate(items):
        sbresult = ""
        if string =="":
            continue
        nums = string.split(",")
        for num in nums:
            try:
                index = int(num)
            except:
                continue

            if index < len(runes_dic):
                s = chr(runes_dic[index])
                sbresult += s

        dict_slice[i] = sbresult

    return dict_slice


def replaceHtmlByDict(origin, dic):
    value = origin
    if re.compile(r"<span class='hs_kw.*?'></span>").search(origin) != None:
        str_matches = re.compile(r"<span class='hs_kw.*?'></span>").findall(origin)

        for str in str_matches:
            tmp = str.replace("<span class='hs_kw", "")
            tmp = tmp.replace("></span>", "")

            str_num = re.compile(r"\d*").findall(tmp)
            num = int(str_num[0])

            if tmp.count("config") > 0:
                if num < len(dic["config"]):
                    str_to_replace = dic["config"][num]
                    value = value.replace(str, str_to_replace)
            elif tmp.count("option") > 0:
                if num < len(dic["option"]):
                    str_to_replace = dic["option"][num]
                    value = value.replace(str, str_to_replace)
            elif tmp.count("keyLink") > 0:
                value = str(dic["keyLink"][num])
        return value
    else:
        return value


def dealAutoHomeItemValue(item, info = {}, key = "", dic = {}):
    id = item["specid"]
    if not(type(id) != None and len(str(id)) != 0):
        return
    car_id = int(id)
    try:
        car = info[car_id]
    except:
        pass
    value = str(item["value"])
    if key == "car_type":
        value = "1"
    if key == "engine_type":
        isexist = 'engine' in car.keys()
        if isexist == True:
            car['engine'] = car['engine']
        else:
            car['engine'] = ""
        value = car["engine"]
    if value != "":
        value = replaceHtmlByDict(value, dic)
    value = replaceDashAsNullString(value)

    car[key] = value







