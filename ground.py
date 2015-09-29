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
date: 2015-09-29 23:30:52
last modified: 2015-09-29 23:46:46
version:
"""

import logging

class Ground(object):
    def __init__(self, line, col):
        self.gen_ground(line, col)

    def gen_ground(self, line, col):
        self.gd = [([0] * col) for i in range(line)]

    def show_ground(self):
        for i in self.gd:
            for j in i:
                print j,
            print

    def set_xy(self, x, y, value):
        self.gd[x][y] = value


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    g = Ground(4, 3)
    g.set_xy(0, 1, 2)
    g.set_xy(1, 0, 3)
    g.show_ground()

if __name__ == '__main__':
    main()
