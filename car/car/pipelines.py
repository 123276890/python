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
        kvs = []
        for k in item:
            k = str(k)
            if k == "settings":
                pass
            else:
                v = item[k]
                v = str(v)
                kv = k + '=' + '"' + v + '"'
                keys.append(k)
                values.append(v)
                kvs.append(kv)
        v = '","'.join(values)
        k = ",".join(keys)
        kv = ",".join(kvs)
        id = item['type_id']

        sql = 'INSERT INTO lrlz_car_crawl(%s) select "%s" from dual where not EXISTS (select 1 from lrlz_car_crawl a where type_id ="%s")' % (k, v, id)
        cur.execute(sql)
        sql1 = 'UPDATE lrlz_car_crawl SET %s WHERE type_id = "%s"' % (kv, id)
        cur.execute(sql1)
        db.commit()
        db.rollback()
        db.close()