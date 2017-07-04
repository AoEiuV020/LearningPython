#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
不知道干嘛用的，
"""
class C:
    def __init__(self, x):
        self._x = x
    @property
    def x(self):
        "I am the 'x' property."
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

c = C(8)
assert c.x == 8
