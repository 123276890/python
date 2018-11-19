# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class CarPipeline(object):
    def process_item(self, item, spider):
        return item


class WebcrawlerScrapyPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='car', charset='utf8')
        cur = db.cursor()
        for key in item:
            key = item[key]
        sql = 'INSERT INTO carDetail(carId,link,carBrand, cars, carName, modelLevel, bodyForm, bodySize, combined, EPStandard, engine, driveAndGearbox, mostPowerful) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        carBrand = item['carBrand']
        cars = item['cars']
        link = item['link']
        carName = item['carName']
        carId = item['carId']
        modelLevel = item['modelLevel']
        bodyForm = item['bodyForm']
        bodySize = item['bodySize']
        combined = item['combined']
        EPStandard = item['EPStandard']
        engine = item['engine']
        driveAndGearbox = item['driveAndGearbox']
        mostPowerful = item['mostPowerful']
        # cur.execute(sql, (cars, link))
        # cur.execute(sql, (carName, link, carId))
        cur.execute(sql, (carId, link, carBrand, cars, carName, modelLevel, bodyForm, bodySize, combined, EPStandard, engine, driveAndGearbox, mostPowerful))
        db.commit()
        db.rollback()
        db.close()