# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
from settings import MYSQL_SETTINGS as ms
from settings import JOB_TABLE
from job_spider import textutils
import dbutils


class JobSpiderPipeline(object):

    def process_item(self, item, spider):
        reload(sys)
        sys.setdefaultencoding('utf8')

        item_dict = textutils.convert(dict(item))

        dbutils.insert(ms, JOB_TABLE, item_dict)

        return item
