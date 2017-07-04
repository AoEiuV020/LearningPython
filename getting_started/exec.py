#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 正常执行，但是没有返回值，

try:
    exec('assert False')
    raise Exception
except AssertionError:
    pass

exec('a = 3')
assert a == 3

e = exec('8')
assert type(e) == type(None)

g = {}
l = {}
exec('global a; a, b = 1, 2', g, l)
assert g['a'] == 1
assert l['b'] == 2
