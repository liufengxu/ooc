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
last modified: 2015-10-01 01:07:04
version:
"""

import logging
import random

import position
import filler


class Ground(object):
    def __init__(self, line, col):
        self.gen_ground(line, col)

    def gen_ground(self, line, col):
        self.map = {}
        self.line = line
        self.col = col
        for i in xrange(self.line):
            for j in xrange(self.col):
                self.map[(i, j)] = position.Position(i, j)

    def show_ground(self):
        for x in xrange(self.line):
            for y in xrange(self.col):
                posi = self.map[(x, y)]
                fill = posi.get_filler()
                if fill:
                    print fill.get_name() + ':' + str(fill.get_hp()),
                else:
                    print '----',
            print

    def bound(self, fill, x, y):
        if (x, y) not in self.map:
            logging.info('Out of range: %s,%s', x, y)
            return False
        posi = self.map[(x, y)]
        fill.set_position(posi)
        posi.set_filler(fill)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    g = Ground(4, 4)
    f1 = filler.Plant('秦', 1, 0)
    f2 = filler.Plant('楚', 1, 0)
    f3 = filler.Plant('燕', 1, 0)
    f4 = filler.Plant('齐', 1, 0)
    f5 = filler.Plant('韩', 1, 0)
    f6 = filler.Plant('赵', 1, 0)
    f7 = filler.Plant('魏', 1, 0)
    g.bound(f1, 2, 0)
    g.bound(f2, 3, 2)
    g.bound(f3, 0, 3)
    g.bound(f4, 1, 3)
    g.bound(f5, 2, 1)
    g.bound(f6, 1, 2)
    g.bound(f7, 2, 2)
    g.show_ground()
    year = 10
    for y in xrange(year):
        logging.info('year:%s', y)
        for i in xrange(g.line):
            for j in xrange(g.col):
                delta = random.randint(-1, 1)
                logging.debug('delta: %s', delta)
                posi = g.map[(i, j)]
                fill = posi.get_filler()
                if fill:
                    fill.grow(delta)
                    logging.debug('%s get delta: %s', fill.get_name(), delta)
                    if fill.is_dead():
                        logging.info('%s 灭亡', fill.get_name())
                        posi.set_filler(None)
                else:
                    logging.debug('delta miss')
        g.show_ground()


if __name__ == '__main__':
    main()
