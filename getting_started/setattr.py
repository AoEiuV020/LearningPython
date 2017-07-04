#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class C:
    i = 0

c = C()
assert c.i == 0
setattr(c, 'i', 1)
assert c.i == 1
# 好像没办法得到对象 c 的名字 c,
exec('c.i = 2')
assert c.i == 2
assert getattr(c, 'i') == 2
