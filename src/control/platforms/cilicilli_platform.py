#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:cilicilli_platform.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2020 by the Niyuhang.
    :license: BSD, see LICENSE for more details.
"""

from AnimeRank.src.control.platforms.base import BasePlatform


class CilicilliPlatform(BasePlatform):

    def crawl(self, *args, **kwargs):
        ...