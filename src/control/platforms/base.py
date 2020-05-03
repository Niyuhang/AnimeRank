#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:base.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2020 by the Niyuhang.
    :license: BSD, see LICENSE for more details.
"""
from abc import ABCMeta, abstractmethod


class BasePlatform(metaclass=ABCMeta):

    @abstractmethod
    def crawl(self, *args, **kwargs):
        ...