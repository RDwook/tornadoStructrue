#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 下午12:10
# @Author  : wook
# @File    : db.py

import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="123123", db="mysql", port=3306, charset="utf8")    # 连接对象

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)

# 关闭数据库连接
# db.close()
