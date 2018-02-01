#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 上午10:43
# @Author  : wook
# @File    : mysql_base
"""
Mysql Table Actions
"""
import pymysql
from cord.database import *


class MysqlBase:
    def __init__(self):
        # Connecting to a database
        self.db = pymysql.connect(host=host, user=user, password=password, db=database, port=port, charset=charset)
        # Creating to a cursor
        self.cursor = self.db.cursor()

    def query_db(self, query):
        return self.cursor.execute(query)

    # Creating a Database
    # def create_db(self, data_base, db_charset='utf8mb4'):
    #     return self.cursor.execute('create database ' + data_base + ' character set ' + db_charset + ';')

    # delete a Database
    # def drop_db(self, data_base):
    #     return self.cursor.execute('drop database ' + ' if exists ' + data_base + ';')

    # Creating a table
    def create_table(self, table, values, primary_key='', engine='InnoDB', character='utf8mb4'):
        table = prefix + table
        # Execute MYSQL using the Execute () method，Delete if Table exists
        self.drop_table(table)
        db_str = 'create table ' + table + '('
        for value in values:
            db_str += value[0] + ' ' + value[1] + ' ' + ('NOT NULL' if value[2] else 'NULL') + ' ' + (
                'AUTO_INCREMENT' if value[3]
                else '') + ','
        if primary_key == '':
            db_str += 'PRIMARY KEY(' + values[0][0] + ')'
        else:
            db_str += 'PRIMARY KEY(' + primary_key + ')'
        db_str += ')ENGINE=' + engine + ' '
        db_str += 'DEFAULT CHARSET=' + character + ';'
        self.cursor.execute(db_str)
        # print(db_str)

    # delete a table
    def drop_table(self, table):
        return self.cursor.execute('drop table ' + ' if exists ' + table + ';')

    def __del__(self):
        # Close a Database
        self.db.close()


if __name__ == "__main__":
    # """create table tro_db(
    #    user_id INT NOT NULL AUTO_INCREMENT,
    #    user_name varchar(40) NOT NULL,
    #    user_password varchar(100) NOT NULL,
    #    user_email varchar(40) NOT NULL,
    #    PRIMARY KEY ( user_id )
    #    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""
    va = [
        ['user_id', 'int(1)', True, True],
        ['user_name', 'varchar(40)', True, False],
        ['user_password', 'varchar(40)', True, False],
        ['user_email', 'varchar(40)', True, False]
    ]
    MysqlBase().create_table('user', va)
