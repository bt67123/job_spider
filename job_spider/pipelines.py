# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import sys
from settings import MYSQL_SETTINGS as ms
from items import Job
from job_spider import textutil
import json


class JobSpiderPipeline(object):

    def process_item(self, item, spider):
        reload(sys)
        sys.setdefaultencoding('utf8')

        item_dict = textutil.convert(dict(item))

        db = pymysql.connect(host=ms['host'],
                             port=ms['port'],
                             user=ms['user'],
                             passwd=ms['passwd'],
                             db=ms['db'],
                             charset=ms['charset'])
        cursor = db.cursor()
        sql = "insert into %s (" % ms['table']
        row = item_dict.keys()
        for i, k in enumerate(row):
            if i == len(row) - 1:
                sql += str(k) + ")"
            else:
                sql += str(k) + ", "

        sql += "values ("

        for i, k in enumerate(row):
            if k in item_dict.keys():
                value = item_dict[k]
                if type(value) == list:
                    value = json.dumps(value, ensure_ascii=False).encode('utf8')
                    value = value.replace("\"", "\\\"")
                    print '**********************************'
                    print value
                    print '**********************************'

                if i == len(row) - 1:
                    sql += "\"" + str(value) + "\"); "
                else:
                    sql += "\"" + str(value) + "\", "
            else:
                if i == len(row) - 1:
                    sql = sql[:len(sql)-2] + ");"

        print '**********************************'
        print sql
        print '**********************************'
        cursor.execute(sql)
        db.commit()
        db.close()

        return item

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False