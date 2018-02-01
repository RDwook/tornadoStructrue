#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 下午1:27
# @Author  : wook
# @File    : db.py
"""
Mysql Operation of the data
"""
from cord.library.mysql.mysqlbase import MysqlBase
from cord.database import prefix


class Db(MysqlBase):
    def __init__(self, table):
        super().__init__()
        self.__table = prefix + table

    # Inserting data
    def insert(self, data_list):
        if type(data_list) == list:
            for d in data_list:
                key_list = '('
                val_list = '('
                for key, value in d.items():
                    key_list += key + ','
                    val_list += "'"+value+"'" + ','
                key_str = key_list[0:-1] + ')'
                val_str = val_list[0:-1] + ')'
                # print('INSERT INTO' + ' ' + self.__table + ' ' + key_str + ' ' + 'VALUES' + ' ' + val_str + ';')
                # noinspection PyBroadException
                try:
                    # Execute MYSQL statement
                    self.cursor.execute(
                        'INSERT INTO' + ' ' + self.__table + ' ' + key_str + ' ' + 'VALUES' + ' ' + val_str + ';')
                    # Commit to Database execution
                    self.db.commit()
                except:
                    # Rollback If an error occurs
                    self.db.rollback()

        else:
            print('Wrong input parameter')

    # Condition
    def where(self, data_list):
        pass

    # Sorting
    def order(self, data_list):
        pass

    # Quantity
    def limit(self, data_list):
        pass

    # Find only one
    def find(self, data_list):
        pass

    # Select data
    def select(self, data_list):
        pass

    # Delete data
    def delete(self, data_list):
        pass

    # Update data
    def update(self, data_list):
        pass

    def __del__(self):
        super().__del__()


if __name__ == '__main__':
    data = [
        {'user_name': 'bar', 'user_password': '123123', 'user_email': 'foo@126.com'},
        {'user_name': 'bar', 'user_password': '123123', 'user_email': 'foo@126.com'},
        {'user_name': 'bar', 'user_password': '123123', 'user_email': 'foo@126.com'},
    ]
    Db('user').insert(data)
