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
        self.condition = ''

    # Inserting data
    def insert(self, data_list):
        if type(data_list) == list:
            for d in data_list:
                key_list = '('
                val_list = '('
                for key, value in d.items():
                    key_list += key + ','
                    val_list += "'" + value + "'" + ','
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

    # Condition AND
    def where(self, condition, binary=False):
        if self.condition.find('WHERE') == -1:
            if binary:
                self.condition += ' WHERE BINARY '
            else:
                self.condition += ' WHERE '
        else:
            self.condition += ' AND '
        self.condition += "(" + condition + ")"
        return self

    # Condition OR
    def where_or(self, condition, binary=False):
        if self.condition.find('WHERE') == -1:
            if binary:
                self.condition += ' WHERE BINARY '
            else:
                self.condition += ' WHERE '
        else:
            self.condition += ' OR '
        self.condition += "(" + condition + ")"
        return self

    # Sorting
    def order(self, data_list):
        pass

    # Quantity
    def limit(self, data_list):
        pass

    # Find only one
    def find(self):
        return self

    # Select data
    def select(self):
        select_str = 'SELECT * from ' + self.__table + '%s;' % self.condition
        # print(select_str)
        try:
            self.cursor.execute(select_str)
            # Output query Results
            self.cursor.fetchall()
            # Cursor positioning (absolute)
            self.cursor.scroll(0, "absolute")
            return self.cursor.fetchall()
        except:
            # Output error
            print("Error: unable to fetch data")

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
        {'user_name': 'arr', 'user_password': '124123', 'user_email': 'fo1@126.com'},
        # {'user_name': 'bar', 'user_password': '123123', 'user_email': 'foo@126.com'},
        # {'user_name': 'bar', 'user_password': '123123', 'user_email': 'foo@126.com'},
    ]

    # insert
    # Db('user').insert(data)

    # select
    sel = Db('user').where("user_name = 'arr'", True).where_or("user_email = 'fo1@126.com'").select()
    print(sel)
