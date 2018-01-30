#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 下午12:10
# @Author  : wook
# @File    : index.py

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render("index.html")
