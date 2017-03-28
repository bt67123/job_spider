# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Job(Item):

    all_keys = [
        'positionId', 'positionName', 'salary',
        'education', 'financeStage', 'city',
        'companyLogo', 'distric', 'companyId',
        'industryField', 'createTime', 'positionLables',
        'workYead', 'lastLogine', 'jobNature',
        'companyFullName', 'companyLabelLis', 'companyShortName',
        'companySized', 'businessZones', 'firstType',
        'secondType', 'positionAdvantage', 'publisherId', 'gradeDescription'
    ]

    positionId = Field()
    positionName = Field()
    salary = Field()
    education = Field()
    financeStage = Field()
    city = Field()
    companyLogo = Field()
    district = Field()
    companyId = Field()
    industryField = Field()
    createTime = Field()
    positionLables = Field()
    workYear = Field()
    lastLogin = Field()
    jobNature = Field()
    companyFullName = Field()
    companyLabelList = Field()
    companyShortName = Field()
    companySize = Field()
    businessZones = Field()
    firstType = Field()
    secondType = Field()
    positionAdvantage = Field()
    publisherId = Field()
    gradeDescription = Field()


"""
 {
                    "companySize": "50-150人",
                    "firstType": "开发/测试/运维类",
                    "appShow": 0,
                    "pcShow": 0,
                    "positionName": "后端开发工程师",
                    "education": "本科",
                    "financeStage": "成长型(B轮)",
                    "city": "深圳",
                    "companyLogo": "i/image/M00/31/BD/Cgp3O1dMCeOAHF9rAAAU-bXZv6s509.jpg",
                    "district": "宝安区",
                    "companyId": 131507,
                    "explain": null,
                    "industryField": "游戏,移动互联网",
                    "createTime": "2017-03-27 19:11:44",
                    "positionLables": [
                        "Java",
                        "J2EE",
                        "后端开发"
                    ],
                    "score": 0,
                    "adWord": 0,
                    "formatCreateTime": "19:11发布",
                    "salary": "9k-18k",
                    "workYear": "3-5年",
                    "lastLogin": 1490612995000,
                    "jobNature": "全职",
                    "deliver": 0,
                    "gradeDescription": null,
                    "imState": "disabled",
                    "companyFullName": "深圳市望尘科技有限公司",
                    "companyLabelList": null,
                    "positionId": 2751332,
                    "companyShortName": "GALASPORTS",
                    "approve": 0,
                    "businessZones": null,
                    "plus": null,
                    "secondType": "后端开发",
                    "positionAdvantage": "周末双休,节假日福利,绩效奖金,五险一金",
                    "publisherId": 5136489,
                    "promotionScoreExplain": null
}
"""
