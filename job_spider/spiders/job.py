# coding:utf-8

from scrapy.spider import Spider
from job_spider.settings import *
from job_spider.items import Job
from scrapy.http import FormRequest
from scrapy.http import Request
from job_spider import dbutils
from scrapy.mail import MailSender
from scrapy.settings import BaseSettings
import json
import math


class JobSpider(Spider):
    name = 'job'
    allowed_domains = ['lagou.com']
    start_urls = [
        'https://www.lagou.com/'
    ]

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip,deflate,sdch,br',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
        'Connection': 'keep-alive',
    }

    def parse(self, response):
        keywords = []
        for sel in response.xpath('//div[@class="menu_sub dn"]/dl'):
            keyword = sel.xpath('dt/a/text()').extract()[0]
            keywords.append(keyword)

            for sel2 in sel.xpath('dd/a'):
                keyword = sel2.xpath('text()').extract()[0]
                keywords.append(keyword)

        job_list_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false' % DEFAULT_CITY
        for keyword in keywords:
            formdata = {'first': 'false', 'pn': '1', 'kd': keyword}
            yield FormRequest(job_list_url,
                              formdata=formdata,
                              headers=self.headers,
                              callback=self.parse_job)

    def parse_job(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        results = jsonresponse['content']['positionResult']['result']
        for result in results:
            job = Job()
            for key in Job.fields.keys():
                if key in result.keys():
                    job[key] = result[key]

            yield job

        # 翻页
        content = jsonresponse['content']
        pr = content['positionResult']
        total = pr.get('totalCount', 0)
        pageSize = content.get('pageSize', 0)
        pageNo = content.get('pageNo', 0)
        keyword = pr.get('queryAnalysisInfo').get('positionName')
        print '**********************************'
        print 'keyword = ' + str(keyword)
        print 'total = ' + str(total)
        print 'pageSize = ' + str(pageSize)
        print 'pageNo = ' + str(pageNo)
        print '**********************************'

        dbutils.insert(MYSQL_SETTINGS, JOB_COUNT_TABLE, {'keyword': keyword, 'total': total})

        if total > 0:
            totalPage = math.ceil(total*1.0/pageSize)
        else:
            totalPage = 0

        print 'totalPage = ' + str(totalPage)

        if totalPage > pageNo and 0 < pageNo < 30:
            job_list_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false' % DEFAULT_CITY
            print '**********************************'
            print 'keyword = ' + keyword
            print 'page = ' + str(pageNo+1)
            print '**********************************'
            formdata = {'first': 'false', 'pn': str(pageNo+1), 'kd': keyword}
            yield FormRequest(job_list_url,
                              formdata=formdata,
                              headers=self.headers,
                              callback=self.parse_job)

    def close(spider, reason):
        settings = BaseSettings({
            'MAIL_FROM': 'cnluocj@aliyun.com',
            'MAIL_HOST': 'smtp.aliyun.com',
            'MAIL_PORT': '25',
            'MAIL_USER': 'cnluocj@aliyun.com',
            'MAIL_PASS': 'Luochujian123456',
        })
        print 'start send email'
        mailer = MailSender.from_settings(settings=settings)
        mailer.send(to=["cnluocj@gmail.com"], subject="job spider end", body=reason)
        print 'end send email'



