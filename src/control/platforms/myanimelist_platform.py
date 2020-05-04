#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:myanimelist_platform.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2020 by the Niyuhang.
    :license: BSD, see LICENSE for more details.
"""
import requests
from AnimeRank.src.control.platforms.base import BasePlatform


class MyanimelistPlatform(BasePlatform):
    ...

    def crawl(self, *args, **kwargs):
        url = "https://myanimelist.net/anime/season/2020/winter"
        res = requests.get(url)
        print(res.text)

    @staticmethod
    def parseHtml(html):
        ...

if __name__ == '__main__':
    pt = MyanimelistPlatform()
    pt.crawl()