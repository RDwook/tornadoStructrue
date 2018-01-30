#!/usr/bin/env Python
# coding=utf-8

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render("index.html")
