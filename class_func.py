# -*- coding: utf-8 -*-
# 类方法
import re
import json
import demjson


class func(object):
    # 类初始化
    def __init__(self):
        pass

    # 价格换算
    def conversion_price(p):
        if type(p) == str:
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

