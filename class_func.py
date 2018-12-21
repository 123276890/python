# -*- coding: utf-8 -*-
# 类方法
import re
import json
import demjson


class func(object):
    # 类初始化
    def __init__(self):
        pass

    # 价格去掉.00
    def price_reduce(p):
        p = p.split('.')
        p = p[0]
        return p

    # 价格换算 万元->元
    def conversion_price(p, isWan=''):
        if type(p) == str and isWan == '':
            # 暂无
            if p.count("暂无") > 0:
               p = "暂无"
            # 厂商指导价：6.58 -> 6.58万元
            elif p.count('厂商') > 0:
                p = p.split("：")
                if p[1].count('万') > 0:
                    p = p[1]
                else:
                    p = p[1] + "万元"
            # 6.58万->65800
            elif p.count('万') > 0:
                p = p.replace('万', '')
                p = int((float(p) + 10 ** -5) * 10000)
            else:
                pass
        # 6.58 -> 65800
        else:
            if p.count('厂商') > 0 and isWan != '':
                p = p.split("：")
                p = p[1].replace('万', '')
                p = int((float(p) + 10 ** -5) * 10000)
            else:
                p = int((float(p) + 10 ** -5) * 10000)
        return p

    # final尾款方案
    def json_final(final_month_price, final_payment, final_period):
        n = [{"final_month_price": final_month_price, "final_payment": final_payment, "final_period": final_period}]
        return n

    # schemes金融方案
    def json_schemes(period, first_price, month_price, first_ratio, final=''):
        if final != '':
            n = {"period": period, "first_price": first_price, "month_price": month_price,
                 "final": final, "first_ratio": first_ratio}
        else:
            n = {'period': period, 'first_price': first_price, 'month_price': month_price, 'first_ratio': first_ratio}

        return n

    # 取出省份 城市 区
    def provinceCity(address):
        p_c_d = []
        province = re.compile(r"(\w+省|\w+自治区|内蒙古|河北)").match(address)

        if province != None:
            province = province.group(1)
            p_c_d.append(province)
            address = address.replace(province, '')
            func.ReCityDistrict(address, p_c_d)
        else:
            func.ReCityDistrict(address, p_c_d)

        return p_c_d

    def ReCityDistrict(address, p_c_d):
        # 直辖市
        central_government = ['北京', '天津', '上海', '重庆']

        city = re.compile(r"(\w+?市|\w+盟|石家庄|张家口)").match(address)
        if city != None:
            city = city.group(1)
            for c in central_government:
                if re.compile(r'%s' % c).search(city) != None:
                    province = city
                    p_c_d.append(province)
                else:
                    pass
            p_c_d.append(city)
            address = address.replace(city, '')
            district = re.compile(r"(\w+?县|\w+?区)").match(address)
            if district != None:
                district = district.group(1)
                if district.count('小区') > 0:
                    pass
                elif district.count('园区') > 0:
                    pass
                elif re.compile(r'[a-zA-Z0-9]区').search(district) != None:
                    pass
                else:
                    p_c_d.append(district)
        else:
            district = re.compile(r"(\w+?县|\w+?区)").match(address)
            if district != None:
                district = district.group(1)
                if district.count('小区') > 0:
                    pass
                elif district.count('园区') > 0:
                    pass
                elif re.compile(r'[a-zA-Z0-9]区').search(district) != None:
                    pass
                else:
                    p_c_d.append(district)
            else:
                pass

        return p_c_d



