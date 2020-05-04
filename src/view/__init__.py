#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:view.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2020 by the Niyuhang.
    :license: BSD, see LICENSE for more details.
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class BasicView(QApplication):
    """
    主view app
    """
    app = layout = None

    def __init__(self, app=None):
        super(BasicView, self).__init__(sys.argv)
        if app:
            self.init_app(app)
        self.init_layout()

    def init_app(self, app):
        """
        初始化app
        :param app:
        :return:
        """
        app.view = self
        self.app = app

    def init_layout(self):
        # 保证view 脱离app也可以独立
        layout = Layout()
        if not self.app:
            title = ""
        else:
            title = self.app.config.get("title")
        layout.setWindowTitle(title)
        self.layout = layout

    def start(self):
        """
        启动主界面
        :return:
        """
        if not self.layout:
            raise ValueError("请初始化layout")
        self.layout.show()
        self.exec_()


class Layout(QMainWindow):
    """
    主视图
    """

    def __init__(self):
        super(Layout, self).__init__()
        self.left = 400


if __name__ == '__main__':
    view = BasicView()
    view.start()
