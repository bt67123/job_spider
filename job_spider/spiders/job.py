# coding:utf-8

from scrapy.spider import Spider
from scrapy.http import HtmlResponse,Request
from job_spider.settings import *
from job_spider.items import Job
from scrapy.http import FormRequest


class JobSpider(Spider):
    name = 'job'
    allowed_domains = ['lagou.com']
    start_urls = [
        'https://www.lagou.com/'
    ]

    def parse(self, response):
        keywords = []
        for sel in response.xpath('//div[@class="menu_sub dn"]/dl'):
            keyword = sel.xpath('dt/a/text()').extract()[0]
            keywords.append(keyword)

            for sel2 in sel.xpath('dd/a'):
                keyword = sel2.xpath('text()').extract()[0]
                keywords.append(keyword)

        job_list_url_form = 'https://www.lagou.com/jobs/list_%s?city=%s'
        for keyword in keywords:
            job_list_url = job_list_url_form % (keyword, DEFAULT_CITY)
            print 'job_list_url => ' + job_list_url
            yield Request(job_list_url, callback=self.parse_job)

    def parse_job(self, response):
        urls = response.xpath('//div[@class="item_con_list"]//a/@href').extract()
        for url in urls:
            if url.endswith('}}.html'):
                pass
            else:
                yield Request(url, callback=self.parse_job_detail)

    def parse_job_detail(self, response):
        job = Job()
        job['name'] = response.xpath('//div[@class="job-name"]/span[@class="name"]/text()').extract()[0]
        job['salary'] = response.xpath('//div[@class="salary"]/text()').extract()[0].strip()
        job['id'] = response.xpath('//input[@id="jobid"]/@value').extract()[0].strip()
        job['company_id'] = response.xpath('//input[@id="companyid"]/@value').extract()[0].strip()
        job['company_name'] = response.xpath('//dl[@id=job_company]//h2/text()').extract()[0].strip()
        yield job

