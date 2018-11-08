# -*- coding: utf-8 -*-


import scrapy
from ..items import CarItem
from scrapy_splash import SplashRequest
from ..autohome import get_complete_text_autohome
import re

script = """
function main(splash)
    splash.images_enabled = false
    splash:go("https://www.autohome.com.cn")
    splash:wait(5)
end
"""


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["autohome.com.cn"]
    url = 'https://www.autohome.com.cn/grade/carhtml/'

    def start_requests(self):
        letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        for lett in letters:
            yield scrapy.Request(url=self.url+lett+'.html', callback=self.parse, meta={'splash': {
                'args': {'lua_source': script},
                'endpoint': 'render.html'
                }
            })

    def parse(self, response):
        for sel in response.xpath('body'):
            item = CarItem()
            brandList = sel.xpath('dl')
            carList = sel.xpath('dl/dd/ul[@class="rank-list-ul"]/li[contains(@id,"s")]')
            for brand in brandList:
                item['carBrand'] = brand.xpath('dd/div[@class="h3-tit"]/a/text()').extract()
                # print(item['carBrand'])
            for cars in carList:
                    item['cars'] = cars.xpath('h4/a/text()').extract()
                    item['link'] = cars.xpath('h4/a/@href')[0].extract()
                    url = response.urljoin(item['link'])
                    # print(item['cars'], url)
                    # yield item
                    yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('//div[@class="carseries-main"]/div[@class="series-list"]')
        item = CarItem()
        if len(detail) > 0:
            names = detail.xpath('div[@class="series-content"]/div[@id="specWrap-2"]/dl/dd/div[@class="spec-name"]/div[@class="name-param"]')
            for name in names:
                name = name.xpath('p')[0]
                item['carId'] = name.xpath('@data-gcjid').extract()
                item['carName'] = name.xpath('a/text()').extract()
                item['link'] = name.xpath('a/@href')[0].extract()
                url = response.urljoin(item['link'])
                # print(item['carId'])
                # print(item['carName'], url)
                # yield item
                yield scrapy.Request(url, meta={'carId': item['carId']}, callback=self.parse_article_detail)
        else:
            detail = response.xpath('//div[@class="title"]/div[@class="title-content"]')
            names = detail.xpath('div')
            for name in names:
                name = name.xpath('div[@class="models"]/div[@class="modelswrap"]/div/div/table/./tr/td[@class="name_d"]/div/a')
                for n in name:
                    item['carName'] = n.xpath('text()').extract()
                    item['link'] = n.xpath('@href')[0].extract()
                    item['carId'] = item['link'][5:-1]
                    url = response.urljoin(item['link'])
                    # print(item['carId'])
                    # yield item
                    yield scrapy.Request(url, meta={'carId': item['carId']}, callback=self.parse_article_detail)
                    # yield scrapy.Request(url='https://www.autohome.com.cn/spec/21220', meta={'carId': item['carId']}, callback=self.parse_article_detail)

    def parse_article_detail(self, response):
        detail = response.xpath('//div[@class="container"]')
        item = CarItem()
        item['carId'] = response.meta['carId']
        item['carBrand'] = detail.xpath('div[@class="container athm-sub-nav article-sub-nav"]/div[@class="athm-sub-nav__car"]/div[@class="athm-sub-nav__car__name"]/a/text()')[0].extract()
        item['carBrand'] = item['carBrand'][:len(item['carBrand'])-1]
        item['cars'] = detail.xpath('div[@class="container athm-sub-nav article-sub-nav"]/div[@class="athm-sub-nav__car"]/div[@class="athm-sub-nav__car__name"]/a/h1/text()')[0].extract()
        item['carName'] = detail.xpath('div[@class="carspec-wrapper"]/div[@class="carspec-main"]/div[@class="spec-information"]/div[@class="information-tit"]/h2/text()')[0].extract()
        baseInfo = detail.xpath('div[@class="carspec-wrapper"]/div[@class="carspec-main"]/div[@class="spec-information"]/div[@class="information-con"]/div[@class="information-summary"]/div[@class="spec-baseinfo"]/ul[@class="baseinfo-list"]/li')
        if baseInfo[0].xpath('text()')[0].extract() == '能源类型：':
            item['energy_type_str'] = baseInfo[0].xpath('span/text()')[0].extract()
            item['mileage'] = baseInfo[1].xpath('span/text()')[0].extract()
            item['slowtime'] = baseInfo[2].xpath('span/text()')[0].extract()
            item['quicktime'] = baseInfo[3].xpath('span/text()')[0].extract()
            item['bat_cap'] = baseInfo[4].xpath('span/text()')[0].extract()
            item['quickpercent'] = baseInfo[5].xpath('span/text()')[0].extract()
            item['quality_guarantee'] = baseInfo[6].xpath('span/text()')[0].extract()
            item['car_size'] = baseInfo[7].xpath('span/text()')[0].extract()
            item['link'] = baseInfo[8].xpath('a/@href')[0].extract()
            url = response.urljoin(item['link'])
            item['bodyForm'] = ''
            item['modelLevel'] = ''

        else:
            item['modelLevel'] = baseInfo[0].xpath('span/text()')[0].extract()
            item['bodyForm'] = baseInfo[1].xpath('span/text()')[0].extract()
            item['bodySize'] = baseInfo[2].xpath('span/text()')[0].extract()
            item['combined'] = baseInfo[3].xpath('span/text()')[0].extract()
            item['EPStandard'] = baseInfo[4].xpath('span/text()')[0].extract()
            item['engine'] = baseInfo[5].xpath('span/text()')[0].extract()
            item['driveAndGearbox'] = baseInfo[6].xpath('span/text()')[0].extract()
            item['mostPowerful'] = baseInfo[7].xpath('span/text()')[0].extract()
            item['link'] = baseInfo[8].xpath('a/@href')[0].extract()
            url = response.urljoin(item['link'])
            item['energy_type_str'] = ''

        yield SplashRequest(url, meta={'energy': item['energy_type_str'], 'bodyForm': item['bodyForm'],
                                       'carId': item['carId'], 'manufacturer': item['carBrand'],
                                       'level': item['modelLevel'], 'carName': item['carName']},
                            callback=self.parse_article_config, args={'wait': 1})

        # print(item['carBrand'], item['cars'], item['carName'], item['modelLevel'], item['bodyForm'], item['bodySize'], item['combined'], item['EPStandard'], item['engine'], item['driveAndGearbox'], item['mostPowerful'], url)
        # yield item

    def parse_article_config(self, response):

        debug_flag = 1

        if 0 or debug_flag:
            # 参数配置
            text = response.body
            text = str(text.decode('utf-8'))
            text = get_complete_text_autohome(text)
            dataConfig = re.search('var config(\s.*?)};', text, re.DOTALL).group()
            dataOption = re.search('var option(\s.*?)};', text, re.DOTALL).group()
            print(dataConfig, dataOption)
            if debug_flag:
                if "hs_kw" not in dataConfig and "hs_kw" not in dataOption:
                    print("%s ok !!" % response.url)
        detailConfig = dataConfig
        detailOption = dataOption
        print(detailConfig, detailOption)

        # if len(detail) > 0:
        #     item = CarItem()
        #     item['type_id'] = response.meta['carId']
        #     item['car_name'] = response.meta['carName']
        #     if len(response.meta['bodyForm']) > 0:
        #         item['car_struct'] = response.meta['bodyForm']
        #     else:
        #         item['car_struct'] = ''
        #     item['manufacturer'] = response.meta['manufacturer']
        #     item['car_level_str'] = response.meta['level']
        #     item['energy_type_str'] = response.meta['energy']
        #     tables = detail.xpath('table')
        #     if len(tables) == 16:
        #         price = tables[0]             # 价格
        #         item['market_price_str'] = price.xpath('tbody/tr[1]/td[1]/div/text()')[0].extract() + '万'
        #         basic = tables[1]             # 基本参数
        #         if len(basic.xpath('tbody/tr')) == 18 and item['energy_type_str'] == '':
        #             print(basic.css("document.styleSheets[1].cssRules[0].selectorText == \"body:before\";"))
        #             item['energy_type_str'] = basic.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['market_time'] = basic.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['max_power'] = basic.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['max_torque'] = basic.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['engine'] = basic.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             item['gearbox'] = basic.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             item['car_size'] = basic.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             if len(item['car_struct']) > 0:
        #                 item['car_struct'] = item['car_struct']
        #             else:
        #                 item['car_struct'] = basic.xpath('tbody/tr[11]/td[1]/div/text()')[0].extract()
        #             item['max_speed'] = basic.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             item['official_speedup'] = basic.xpath('tbody/tr[13]/td[1]/div/text()').extract()
        #             item['actual_speedup'] = basic.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #             item['actual_brake'] = basic.xpath('tbody/tr[15]/td[1]/div/text()').extract()
        #             item['gerenal_fueluse'] = basic.xpath('tbody/tr[16]/td[1]/div/text()').extract()
        #             item['actual_fueluse'] = basic.xpath('tbody/tr[17]/td[1]/div/text()').extract()
        #             item['quality_guarantee'] = basic.xpath('tbody/tr[18]/td[1]/div/text()').extract()
        #
        #             # print(item['type_id'], item['car_name'], item['market_price_str'], item['manufacturer'],
        #             #       item['car_level_str'], item['energy_type_str'], item['max_power'], item['max_torque'],
        #             #       item['engine'], item['gearbox'], item['car_size'], item['car_struct'], item['max_speed'],
        #             #       item['official_speedup'], item['actual_speedup'], item['actual_brake'],
        #             #       item['gerenal_fueluse'], item['actual_fueluse'], item['quality_guarantee'])
        #
        #         elif len(basic.xpath('tbody/tr')) == 18 and len(item['energy_type_str']) > 0:
        #             item['energy_type_str'] = basic.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['market_time'] = basic.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['e_mileage'] = basic.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['quicktime'] = basic.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['slowtime'] = basic.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             item['quickpercent'] = basic.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             item['max_power'] = basic.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             item['max_torque'] = basic.xpath('tbody/tr[11]/td[1]/div/text()').extract()
        #             item['car_size'] = basic.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             if len(item['car_struct']) > 0:
        #                 item['car_struct'] = item['car_struct']
        #             else:
        #                 item['car_struct'] = basic.xpath('tbody/tr[13]/td[1]/div/text()')[0].extract()
        #             item['max_speed'] = basic.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #             item['official_speedup'] = basic.xpath('tbody/tr[15]/td[1]/div/text()').extract()
        #             item['actual_speedup'] = basic.xpath('tbody/tr[16]/td[1]/div/text()').extract()
        #             item['actual_brake'] = basic.xpath('tbody/tr[17]/td[1]/div/text()').extract()
        #             item['quality_guarantee'] = basic.xpath('tbody/tr[18]/td[1]/div/text()').extract()
        #
        #         elif len(basic.xpath('tbody/tr')) == 17:
        #             item['energy_type_str'] = basic.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['max_power'] = basic.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['max_torque'] = basic.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['engine'] = basic.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['gearbox'] = basic.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             item['car_size'] = basic.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             if len(item['car_struct']) > 0:
        #                 item['car_struct'] = item['car_struct']
        #             else:
        #                 item['car_struct'] = basic.xpath('tbody/tr[10]/td[1]/div/text()')[0].extract()
        #             item['max_speed'] = basic.xpath('tbody/tr[11]/td[1]/div/text()').extract()
        #             item['official_speedup'] = basic.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             item['actual_speedup'] = basic.xpath('tbody/tr[13]/td[1]/div/text()').extract()
        #             item['actual_brake'] = basic.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #             item['gerenal_fueluse'] = basic.xpath('tbody/tr[15]/td[1]/div/text()').extract()
        #             item['actual_fueluse'] = basic.xpath('tbody/tr[16]/td[1]/div/text()').extract()
        #             item['quality_guarantee'] = basic.xpath('tbody/tr[17]/td[1]/div/text()').extract()
        #
        #         elif len(basic.xpath('tbody/tr')) == 19:
        #             item['energy_type_str'] = basic.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['market_time'] = basic.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['e_mileage'] = basic.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['max_power'] = basic.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             item['max_torque'] = basic.xpath('tbody/tr[11]/td[1]/div/text()').extract()
        #             item['car_size'] = basic.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             if len(item['car_struct']) > 0:
        #                 item['car_struct'] = item['car_struct']
        #             else:
        #                 item['car_struct'] = basic.xpath('tbody/tr[13]/td[1]/div/text()')[0].extract()
        #             item['max_speed'] = basic.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #             item['official_speedup'] = basic.xpath('tbody/tr[15]/td[1]/div/text()').extract()
        #             item['actual_speedup'] = basic.xpath('tbody/tr[16]/td[1]/div/text()').extract()
        #             item['actual_brake'] = basic.xpath('tbody/tr[17]/td[1]/div/text()').extract()
        #             item['quality_guarantee'] = basic.xpath('tbody/tr[19]/td[1]/div/text()').extract()
        #
        #         elif len(basic.xpath('tbody/tr')) == 21:
        #             item['energy_type_str'] = basic.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['market_time'] = basic.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['e_mileage'] = basic.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['quicktime'] = basic.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['slowtime'] = basic.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             item['quickpercent'] = basic.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             item['max_power'] = basic.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             item['max_torque'] = basic.xpath('tbody/tr[11]/td[1]/div/text()').extract()
        #             item['car_size'] = basic.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             if len(item['car_struct']) > 0:
        #                 item['car_struct'] = item['car_struct']
        #             else:
        #                 item['car_struct'] = basic.xpath('tbody/tr[13]/td[1]/div/text()')[0].extract()
        #             item['max_speed'] = basic.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #             item['official_speedup'] = basic.xpath('tbody/tr[15]/td[1]/div/text()').extract()
        #             item['actual_speedup'] = basic.xpath('tbody/tr[16]/td[1]/div/text()').extract()
        #             item['actual_brake'] = basic.xpath('tbody/tr[17]/td[1]/div/text()').extract()
        #             item['quality_guarantee'] = basic.xpath('tbody/tr[21]/td[1]/div/text()').extract()
        #
        #         elif len(basic.xpath('tbody/tr')) == 25 and len(item['energy_type_str']) > 2:
        #             item['energy_type_str'] = basic.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['market_time'] = basic.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['e_mileage'] = basic.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['quicktime'] = basic.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['slowtime'] = basic.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             item['quickpercent'] = basic.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             item['max_power'] = basic.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             item['max_torque'] = basic.xpath('tbody/tr[11]/td[1]/div/text()').extract()
        #             item['engine'] = basic.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             item['gearbox'] = basic.xpath('tbody/tr[13]/td[1]/div/text()').extract()
        #             item['car_size'] = basic.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #             if len(item['car_struct']) > 0:
        #                 item['car_struct'] = item['car_struct']
        #             else:
        #                 item['car_struct'] = basic.xpath('tbody/tr[15]/td[1]/div/text()')[0].extract()
        #             item['max_speed'] = basic.xpath('tbody/tr[16]/td[1]/div/text()').extract()
        #             item['official_speedup'] = basic.xpath('tbody/tr[17]/td[1]/div/text()').extract()
        #             item['actual_speedup'] = basic.xpath('tbody/tr[18]/td[1]/div/text()').extract()
        #             item['actual_brake'] = basic.xpath('tbody/tr[19]/td[1]/div/text()').extract()
        #             item['gerenal_fueluse'] = basic.xpath('tbody/tr[23]/td[1]/div/text()').extract()
        #             item['actual_fueluse'] = basic.xpath('tbody/tr[24]/td[1]/div/text()').extract()
        #             item['quality_guarantee'] = basic.xpath('tbody/tr[25]/td[1]/div/text()').extract()
        #
        #         else:
        #             item['energy_type_str'] = basic.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['market_time'] = basic.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['max_power'] = basic.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['max_torque'] = basic.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['engine'] = basic.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             item['gearbox'] = basic.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             item['car_size'] = basic.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             if len(item['car_struct']) > 0:
        #                 item['car_struct'] = item['car_struct']
        #             else:
        #                 item['car_struct'] = basic.xpath('tbody/tr[11]/td[1]/div/text()')[0].extract()
        #             item['max_speed'] = basic.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             item['gerenal_fueluse'] = basic.xpath('tbody/tr[13]/td[1]/div/text()').extract()
        #             item['quality_guarantee'] = basic.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #
        #         if len(item['quality_guarantee']) > 1:
        #             item['quality_guarantee'] = item['quality_guarantee'][0] + '年或' + item['quality_guarantee'][1] + '万' + item['quality_guarantee'][2]
        #         else:
        #             item['quality_guarantee'] = item['quality_guarantee'][0] + '年不限公里'
        #
        #             # print(item['type_id'], item['car_name'], item['market_price_str'], item['manufacturer'],
        #             #       item['car_level_str'], item['energy_type_str'], item['max_power'], item['max_torque'],
        #             #       item['engine'], item['gearbox'], item['car_size'], item['car_struct'], item['max_speed'],
        #             #       item['gerenal_fueluse'], item['quality_guarantee'])
        #
        #         if len(item['car_struct']) > 3 and item['car_struct'] != '暂无':
        #             item['body_struct'] = re.compile(r"[\u5ea7]+.*").findall(item['car_struct'])[0][1:]
        #         elif len(item['car_struct']) > 0 and item['car_struct'] != '暂无':
        #             item['body_struct'] = item['car_struct']
        #         else:
        #             item['body_struct'] = ''
        #
        #         body = tables[2]              # 车身
        #         if len(body.xpath('tbody/tr')) == 16:
        #             item['length'] = body.xpath('tbody/tr[2]/td[1]/div/text()').extract()
        #             item['width'] = body.xpath('tbody/tr[3]/td[1]/div/text()').extract()
        #             item['height'] = body.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['shaft_distance'] = body.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['front_wheels_gap'] = body.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['back_wheels_gap'] = body.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['min_ground'] = body.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             item['total_weight'] = body.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             if len(item['body_struct']) > 0:
        #                 item['body_struct'] = item['body_struct']
        #             else:
        #                 item['body_struct'] = body.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             item['doors'] = body.xpath('tbody/tr[11]/td[1]/div/text()').extract()
        #             item['seats'] = body.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             item['open_type'] = body.xpath('tbody/tr[13]/td[1]/div/text()').extract()
        #             item['fuel_vol'] = body.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #             item['cargo_size'] = body.xpath('tbody/tr[15]/td[1]/div/text()').extract()
        #             item['carry_cap'] = body.xpath('tbody/tr[16]/td[1]/div/text()').extract()
        #             # print(item['type_id'], item['body_struct'], item['quality_guarantee'], item['length'], item['width'], item['height'],
        #             #       item['shaft_distance'], item['front_wheels_gap'], item['back_wheels_gap'], item['min_ground'],
        #             #       item['total_weight'], item['doors'], item['seats'], item['open_type'], item['fuel_vol'],
        #             #       item['cargo_size'], item['carry_cap'])
        #
        #         else:
        #             item['length'] = body.xpath('tbody/tr[2]/td[1]/div/text()').extract()
        #             item['width'] = body.xpath('tbody/tr[3]/td[1]/div/text()').extract()
        #             item['height'] = body.xpath('tbody/tr[4]/td[1]/div/text()').extract()
        #             item['shaft_distance'] = body.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['front_wheels_gap'] = body.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['back_wheels_gap'] = body.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['min_ground'] = body.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             if len(item['body_struct']) > 0:
        #                 item['body_struct'] = item['body_struct']
        #             else:
        #                 item['body_struct'] = body.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             item['doors'] = body.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             item['seats'] = body.xpath('tbody/tr[11]/td[1]/div/text()').extract()
        #             item['fuel_vol'] = body.xpath('tbody/tr[12]/td[1]/div/text()').extract()
        #             item['cargo_vol'] = body.xpath('tbody/tr[13]/td[1]/div/text()').extract()
        #             item['total_weight'] = body.xpath('tbody/tr[14]/td[1]/div/text()').extract()
        #
        #             # print(item['type_id'], item['body_struct'], item['quality_guarantee'], item['length'], item['width'], item['height'],
        #             #       item['shaft_distance'], item['front_wheels_gap'], item['back_wheels_gap'], item['min_ground'],
        #             #       item['total_weight'], item['doors'], item['seats'], item['fuel_vol'], item['cargo_vol'])
        #
        #         engine = tables[3]            # 发动机
        #         if len(engine.xpath('tbody/tr')) == 16:
        #             item['engine_type'] = item['engine']
        #             item['cc'] = engine.xpath('tbody/tr[3]/td[1]/div/text()').extract()
        #             item['air_intake'] = engine.xpath('tbody/tr[5]/td[1]/div/text()').extract()
        #             item['cylinder_arrange'] = engine.xpath('tbody/tr[6]/td[1]/div/text()').extract()
        #             item['cylinders'] = engine.xpath('tbody/tr[7]/td[1]/div/text()').extract()
        #             item['valves'] = engine.xpath('tbody/tr[8]/td[1]/div/text()').extract()
        #             item['compress_rate'] = engine.xpath('tbody/tr[9]/td[1]/div/text()').extract()
        #             item['valve_machanism'] = engine.xpath('tbody/tr[10]/td[1]/div/text()').extract()
        #             item['cylinder_radius'] = engine.xpath('tbody/tr[11]/td[1]/div/text()').extract()
        #             item['environmental_standard'] = engine.xpath('tbody/tr[24]/td[1]/div').extract()
        #
        #         transmission = tables[4]      # 变速箱
        #         chassis = tables[5]           # 底盘转向
        #         wheels = tables[6]            # 车轮制动
        #         safety = tables[7]            # 主/被动安全装备
        #         manipulation = tables[8]      # 辅助/操控配置
        #         gat = tables[9]               # 外部/防盗配置
        #         internal = tables[10]         # 内部配置
        #         seat = tables[11]             # 座椅配置
        #         multimedia = tables[12]       # 多媒体配置
        #         light = tables[13]            # 灯光配置
        #         glass = tables[14]            # 玻璃/后视镜
        #         refrigerator = tables[15]     # 空调/冰箱
        #
        #     elif len(tables) == 17 and len(item['energy_type_str']) > 0:
        #         price = tables[0]             # 价格
        #         basic = tables[1]             # 基本参数
        #         body = tables[2]              # 车身
        #         engine = tables[3]            # 发动机
        #         motor = tables[4]             # 电动机
        #         transmission = tables[5]      # 变速箱
        #         chassis = tables[6]           # 底盘转向
        #         wheels = tables[7]            # 车轮制动
        #         safety = tables[8]            # 主/被动安全装备
        #         manipulation = tables[9]      # 辅助/操控配置
        #         gat = tables[10]              # 外部/防盗配置
        #         internal = tables[11]         # 内部配置
        #         seat = tables[12]             # 座椅配置
        #         multimedia = tables[13]       # 多媒体配置
        #         light = tables[14]            # 灯光配置
        #         glass = tables[15]            # 玻璃/后视镜
        #         refrigerator = tables[16]     # 空调/冰箱
        #
        #     elif len(tables) == 17 and len(item['energy_type_str']) == 0:
        #        price = tables[0]              # 价格
        #        basic = tables[1]              # 基本参数
        #        body = tables[2]               # 车身
        #        transmission = tables[3]       # 变速箱
        #        chassis = tables[4]            # 底盘转向
        #        wheels = tables[5]             # 车轮制动
        #        engine = tables[6]             # 发动机
        #        motor = tables[7]              # 电动机
        #        safety = tables[8]             # 主/被动安全装备
        #        manipulation = tables[9]       # 辅助/操控配置
        #        gat = tables[10]               # 外部/防盗配置
        #        internal = tables[11]          # 内部配置
        #        seat = tables[12]              # 座椅配置
        #        multimedia = tables[13]        # 多媒体配置
        #        light = tables[14]             # 灯光配置
        #        glass = tables[15]             # 玻璃/后视镜
        #        refrigerator = tables[16]      # 空调/冰箱
        #
        #     else:
        #         pass


