#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 上午8:51
# @Author  : wook
# @File    : path.py
"""
Path simplification
"""
from cord.config import *


def admin_path(name):
    return 'admin/' + name + file_root


def index_path(name):
    return 'index/' + name + file_root
