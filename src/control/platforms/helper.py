#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:helper.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2020 by the Niyuhang.
    :license: BSD, see LICENSE for more details.
"""

import importlib
import os
import re
import logging

from os import path

from AnimeRank.src.const import PLATFORM_MODULE_PATH

logger = logging.getLogger(__name__)


def import_the_platform(name):
    try:
        module = importlib.import_module("{}.{}_platform".format(PLATFORM_MODULE_PATH, name))
        platform = getattr(module, "{}Platform".format(name.capitalize()))
        return platform
    except Exception as e:
        logger.error(e)


def get_all_platforms():
    """
    :return: [Object<Platform>]
    """
    res = []
    platform_dir_path = path.dirname(path.abspath(__file__))
    files = os.listdir(platform_dir_path)
    # 加载所有platform
    pattern = re.compile(r"^([a-zA-Z]+)_platform\.py$")
    for file_name in files:
        search_module_name = pattern.match(file_name)
        if search_module_name:
            module_name = search_module_name.groups()[0]
            logger.info("get module name, {}".format(module_name))
            platform = import_the_platform(module_name)
            res.append(platform) if platform else None
    return res


if __name__ == '__main__':
    platforms = get_all_platforms()
    print(platforms)