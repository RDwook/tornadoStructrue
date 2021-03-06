#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 下午12:10
# @Author  : wook
# @File    : application.py

from cord.url import url

import tornado.web
import os

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "../templates"),
    static_path=os.path.join(os.path.dirname(__file__), "../statics"),
    # debug=True
    )

application = tornado.web.Application(
    handlers=url,
    **settings
    )
