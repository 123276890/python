# -*- coding: utf-8 -*-
# 类方法


class func(object):
    # 价格转换 例6.58万->65800
    def conversion_price(p):
        p = p.replace('万', '')
        p = int((float(p) + 10 ** -5) * 10000)
        return p

    # schemes方案
    def json_schemes(period, first_price, month_price, final, first_ratio):
        if len(final) > 0:
            n = {"period": period, "first_price": first_price, "month_price": month_price,
                 "final": final, "first_ratio": first_ratio}
        else:
            n = {'period': period, 'first_price': first_price, 'month_price': month_price, 'first_ratio': first_ratio}

    # final
    def json_final(final_month_price, final_payment, final_period):
        n = [{"final_month_price": final_month_price, "final_payment": final_payment, "final_period": final_period}]