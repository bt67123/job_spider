# coding:utf-8

from scrapy.spider import Spider
from scrapy.http import HtmlResponse,Request
from job_spider.settings import *
from job_spider.items import Job
from scrapy.http import FormRequest
from cookielib import CookieJar
import json
import random


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

    cookies = {
        'user_trace_token': '20170326232733-7b144a277697485ba8693c95d7097ea5',
        'LGUID': '20170326232734-bc595a50-1238-11e7-a251-525400f775ce',
        'index_location_city': '%E6%B7%B1%E5%9C%B3',
        'TG-TRACK-CODE': 'index_navigation',
        'SEARCH_ID': '5951c5f55df64bbda9043fcd9ccc9a7b',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1490542064',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1490542122',
        '_ga': 'GA1.2.1638570626.1490542064',
        'LGRID': '20170326232832-dee75d3d-1238-11e7-956f-5254005c3644',
        'JSESSIONID': '1CA02935D797115D2CF33B65E763316D',
    }

    user_agent_list = [\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]

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
            ua = random.choice(self.user_agent_list)
            self.headers['User-Agent'] = ua
            formdata = {'first': 'false', 'pn': '1', 'kd': keyword}
            yield FormRequest(job_list_url,
                              formdata=formdata,
                              cookies=self.cookies,
                              headers=self.headers,
                              callback=self.parse_job)

    def parse_job(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        job = Job()
        job['name'] =jsonresponse['content']
        yield job

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

# job_list_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
