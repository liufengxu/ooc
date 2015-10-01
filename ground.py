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
last modified: 2015-10-01 23:54:42
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
                    print fill.get_name() + str(fill.age) + ':' + \
                          str(fill.get_hp()),
                else:
                    print '-----',
            print

    def bound(self, fill, x, y):
        if (x, y) not in self.map:
            logging.info('Out of range: %s,%s', x, y)
            return False
        posi = self.map[(x, y)]
        fill.set_position(posi)
        posi.set_filler(fill)

    def pass_years(self, year_num):
        for year in xrange(1, year_num + 1):
            logging.info('year:%s', year)
            for i in xrange(self.line):
                for j in xrange(self.col):
                    delta = random.randint(-1, 1)
                    logging.debug('delta: %s', delta)
                    posi = self.map[(i, j)]
                    fill = posi.get_filler()
                    if fill:
                        fill.grow(delta)
                        logging.debug('%s get delta: %s', fill.get_name(),
                                      delta)
                        if fill.is_dead():
                            logging.info('%s 灭亡', fill.get_name())
                            fill.set_age(fill.get_age() + 1)
                            fill.set_hp(1)
                        elif fill.get_hp() >= 10:
                            posi = self.get_random_empty()
                            if posi:
                                new_f = filler.Plant(fill.get_name() +
                                                     str(fill.get_age()) +
                                                     's', 1, 0)
                                self.bound(new_f, posi.get_xy()[0],
                                           posi.get_xy()[1])
                                logging.info('分支创立 %s', new_f.get_name())
                    else:
                        logging.debug('delta miss')
            self.show_ground()

    def get_random_empty(self):
        empty_list = []
        for x in xrange(self.line):
            for y in xrange(self.col):
                posi = self.map[(x, y)]
                fill = posi.get_filler()
                if not fill:
                    empty_list.append(posi)
        if empty_list:
            return random.choice(empty_list)
        return None


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
    g.pass_years(30)


if __name__ == '__main__':
    main()
