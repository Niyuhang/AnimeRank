#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:app.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2020 by the Niyuhang.
    :license: BSD, see LICENSE for more details.
"""
from AnimeRank.src.view import BasicView
from AnimeRank.src.const import TITLE

from flask import Flask
class App:
    """
    App
    """

    def __init__(self, title=None):
        # todo: 配置初始参数
        # 先初始化config
        self.config = {}
        self.config.update({"title": title or TITLE})

        self.init_view()

    def init_view(self):
        BasicView(self)

    def run(self):
        self.view.start()


def create_app():
    app = App()
    return app

