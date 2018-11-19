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
        keys = []
        values = []
        for k in item:
            k = str(k)
            if k == "settings":
                pass
            else:
                v = item[k]
                v = str(v)
                keys.append(k)
                values.append(v)
        v = '","'.join(values)
        k = ",".join(keys)
        sql = 'INSERT INTO lrlz_car_crawl(%s) VALUE ("%s")' % (k, v)
        cur.execute(sql)
        db.commit()
        db.rollback()
        db.close()