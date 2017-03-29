# coding:utf-8

import pymysql
import json


def insert(ms, table, data):

    db = pymysql.connect(host=ms['host'],
                         port=ms['port'],
                         user=ms['user'],
                         passwd=ms['passwd'],
                         db=ms['db'],
                         charset=ms['charset'])
    cursor = db.cursor()
    sql = "insert into %s (" % table
    row = data.keys()
    for i, k in enumerate(row):
        if i == len(row) - 1:
            sql += str(k) + ")"
        else:
            sql += str(k) + ", "

    sql += "values ("

    for i, k in enumerate(row):
        if k in data.keys():
            value = data[k]
            if type(value) == list:
                value = json.dumps(value, ensure_ascii=False).encode('utf8')
                value = value.replace("\"", "\\\"")
                # print '**********************************'
                # print value
                # print '**********************************'

            if i == len(row) - 1:
                sql += "\"" + str(value) + "\"); "
            else:
                sql += "\"" + str(value) + "\", "
        else:
            if i == len(row) - 1:
                sql = sql[:len(sql) - 2] + ");"

    # print '**********************************'
    # print sql
    # print '**********************************'
    cursor.execute(sql)
    db.commit()
    db.close()
