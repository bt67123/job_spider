# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Job(Item):
    id = Field()
    name = Field()
    salary = Field()
    company_id = Field()
    company_name = Field()


class Company(Item):
    id = Field()
    name = Field()
    type = Field()
    process = Field()
    number = Field()
    address = Field()
    tags = Field()
    # 处理率
    rate = Field()
    # 处理用时
    spend_time = Field()
    # 评价数
    eval_num = Field()


class JobKeyword(Item):
    name = Field()
