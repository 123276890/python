# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class ProjecthuxiuPipeline(object):
    def process_item(self, item, spider):
        return item

class WebcrawlerScrapyPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='demo', charset='utf8')
        cur = db.cursor()
        sql = 'INSERT INTO huxiu(title,link,posttime) VALUES (%s,%s,%s)'
        # sql = 'INSERT INTO test(title,link) VALUES (%s,%s)'
        title = item['title']
        link = item['link']
        posttime = item['posttime']
        cur.execute(sql, (title, link, posttime))
        # cur.execute(sql, (title, link))
        db.commit()
        db.rollback()
        db.close()
