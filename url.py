#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 下午12:10
# @Author  : wook
# @File    : url.py
"""
the url structure of website
"""

from handlers.index import IndexHandler

url = [
    (r'/', IndexHandler),
]
