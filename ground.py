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
last modified: 2015-09-30 23:55:45
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
        self.line = line
        self.col = col
        self.gd = [([None] * col) for i in range(line)]

    def show_ground(self):
        for i in self.gd:
            for j in i:
                if j:
                    print j.get_name() + ':' + str(j.get_hp()),
                else:
                    print '----',
            print

    def set_filler(self, filler):
        position = filler.get_position()
        x, y = position.get_xy()
        if x >= self.line or y >= self.col:
            logging.debug('Position x,y:%s,%s is out of the ground', x, y)
            return False
        if self.gd[x][y]:
            logging.debug('Position x,y:%s,%s is taken', x, y)
            return False
        self.gd[x][y] = filler


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    g = Ground(4, 4)
    p1 = position.Position(2, 0)
    p2 = position.Position(3, 2)
    p3 = position.Position(0, 3)
    p4 = position.Position(1, 3)
    p5 = position.Position(2, 1)
    p6 = position.Position(1, 2)
    p7 = position.Position(2, 2)
    f1 = filler.Plant('秦', 1, 0)
    f2 = filler.Plant('楚', 1, 0)
    f3 = filler.Plant('燕', 1, 0)
    f4 = filler.Plant('齐', 1, 0)
    f5 = filler.Plant('韩', 1, 0)
    f6 = filler.Plant('赵', 1, 0)
    f7 = filler.Plant('魏', 1, 0)
    f1.set_position(p1)
    f2.set_position(p2)
    f3.set_position(p3)
    f4.set_position(p4)
    f5.set_position(p5)
    f6.set_position(p6)
    f7.set_position(p7)
    g.set_filler(f1)
    g.set_filler(f2)
    g.set_filler(f3)
    g.set_filler(f4)
    g.set_filler(f5)
    g.set_filler(f6)
    g.set_filler(f7)
    g.show_ground()
    year = 10
    for y in xrange(year):
        logging.info('year:%s', y)
        for i in g.gd:
            for j in i:
                delta = random.randint(-1, 1)
                logging.debug('delta: %s', delta)
                if j:
                    j.grow(delta)
                    logging.debug('%s get delta: %s', j.get_name(), delta)
                    if j.is_dead():
                        logging.info('%s 灭亡', j.get_name())
                else:
                    logging.debug('delta miss')
        g.show_ground()


if __name__ == '__main__':
    main()
