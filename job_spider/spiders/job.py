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

        # job_list_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
        job_list_url = 'https://www.lagou.com/jobs/positionAjax.json?city=深圳&needAddtionalResult=false'
        for keyword in keywords:
            formdata = {'first': False, 'pn': 1, 'kd': keyword}
            yield FormRequest(job_list_url, formdata=formdata, callback=self.parse_job)

    def parse_job(self, response):
        yield response

    def parse_job_detail(self, response):
        job = Job()
        job['name'] = response.xpath('//div[@class="job-name"]/span[@class="name"]/text()').extract()[0]
        job['salary'] = response.xpath('//div[@class="salary"]/text()').extract()[0].strip()
        job['id'] = response.xpath('//input[@id="jobid"]/@value').extract()[0].strip()
        job['company_id'] = response.xpath('//input[@id="companyid"]/@value').extract()[0].strip()
        job['company_name'] = response.xpath('//dl[@id=job_company]//h2/text()').extract()[0].strip()
        yield job


# post 请求
#
# In [1]: from scrapy.http import FormRequest
#
# In [2]: frmdata = {"id": "com.supercell.boombeach", "reviewType": '0', "reviewSortOrder": '0', "pageNum":'0'}
#
# In [3]: url = "https://play.google.com/store/getreviews"
#
# In [4]: r = FormRequest(url, formdata=frmdata)

