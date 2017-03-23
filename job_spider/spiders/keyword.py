# coding:utf-8

from scrapy.spider import Spider
from job_spider.items import JobKeyword


class KeywordSpider(Spider):
    name = 'keyword'
    allowed_domains = ['lagou.com']
    start_urls = [
        'https://www.lagou.com/'
    ]

    def parse(self, response):
        items = []
        for sel in response.xpath('//div[@class="menu_sub dn"]/dl'):
            item = JobKeyword()
            item['name'] = sel.xpath('dt/a/text()').extract()[0]
            items.append(item)

            for sel2 in sel.xpath('dd/a'):
                item = JobKeyword()
                item['name'] = sel2.xpath('text()').extract()[0]
                items.append(item)

        return items



