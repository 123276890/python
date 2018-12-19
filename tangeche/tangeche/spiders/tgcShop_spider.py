# -*- coding: utf-8 -*-

import requests
import json
from ..items import TgcShopItem


class tgcShop():
    def tgc_shop(total_page, carId):
        shopList = []
        for page in range(1, total_page):
            content = {'modelCode': carId, 'page': page, 'pageSize': 100}
            url = 'https://leaseconsumer.souche.com//v1/followShopApi/getShopPage.json'
            result = requests.post(url, data=content)
            shopData = (json.loads(result.text))['data']['items']

            for shop in shopData:
                itemS = TgcShopItem()
                itemS['source_id'] = 2
                itemS['original_id'] = shop['shopCode']
                shop_type = shop['shop4S']
                if shop_type == False:
                    itemS['shop_type'] = 1
                else:
                    itemS['shop_type'] = 0
                itemS['shop_name'] = shop['shopName']
                cityName = shop['cityName'].split()
                try:
                    itemS['shop_province'] = cityName[0]
                except:
                    print(cityName)
                itemS['shop_city'] = cityName[1]
                try:
                    itemS['shop_district'] = cityName[2]
                except:
                    itemS['shop_district'] = ''
                itemS['shop_address'] = shop['shopAddr']
                itemS['shop_telphone'] = shop['contactTel']
                shopList.append(itemS)

        return shopList
