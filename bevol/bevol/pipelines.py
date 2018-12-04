# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time



class BevolPipeline(object):
    def process_item(self, item, spider):
        return item


class WebcrawlerScrapyPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='car_local', charset='utf8')
        cur = db.cursor()
        keys = []
        values = []
        kvs = []
        for k in item:
            v = item[k]
            v = str(v)
            kv = k + '=' + "'" + v + "'"
            keys.append(k)
            values.append(v)
            kvs.append(kv)
        v = "','".join(values)
        k = ",".join(keys)
        kv = ",".join(kvs)
        id = item['cosmetics_id']
        sql = "INSERT INTO bevol(%s) select '%s' from dual where not EXISTS (select 1 from bevol a where cosmetics_id ='%s')" % (k, v, id)
        cur.execute(sql)
        now = int(round(time.time() * 1000))
        updatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
        kv = kv + ',' + "update_time" + '=' + "'" + updatetime + "'"
        sql1 = "UPDATE bevol SET %s WHERE cosmetics_id = '%s'" % (kv, id)
        cur.execute(sql1)
        db.commit()
        db.rollback()
        db.close()
