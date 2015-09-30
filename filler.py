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
date: 2015-09-30 16:44:38
last modified: 2015-09-30 23:36:34
version:
"""

import logging


class Filler(object):
    def __init__(self, name):
        self.set_name(name)
        self.position = None

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Plant(Filler):
    def __init__(self, name, hp, age):
        Filler.__init__(self, name)
        self.set_age(age)
        self.set_hp(hp)

    def set_hp(self, hp):
        self.hp = hp

    def set_age(self, age):
        self.age = age

    def get_hp(self):
        return self.hp

    def get_age(self):
        return self.age

    def grow(self, delta):
        self.hp += delta

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    main()
