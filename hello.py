#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 上午11:41
# @Author  : wook
# @File    : hello.py
"""
test
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', welcome you to read')


if __name__ == "__main__":
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
