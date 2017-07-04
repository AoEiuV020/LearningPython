#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class C:
    i = 0

c = C()
assert getattr(c, 'i') == 0
# 好像没办法得到对象 c 的名字 c,
assert eval('c.i') == 0
