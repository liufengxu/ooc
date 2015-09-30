#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2015 .com, Inc. All Rights Reserved
#
################################################################################
"""
description:
author: liufengxu
date: 2015-09-30 16:29:42
last modified: 2015-09-30 23:08:20
version:
"""

import logging

class Position(object):
    def __init__(self, x, y):
        self.set_xy(x, y)

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def get_xy(self):
        return (self.x, self.y)

def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    main()
