#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert type((1, 2)) == tuple
t = (1, 2)
assert t[0] == 1
assert t[1] == 2
t = 1, 2
assert t == (1, 2)
assert list((0, 1, 2, 3, 4)) == list(range(5))

t = 1, 2
a, b = t
assert a == 1
assert b == 2

assert len((1, )) == 1
assert (1,)[0] == 1

assert tuple(range(1)) == (0,)
assert tuple(range(2)) == (0, 1)
try:
    (1,)[0] = 0
except TypeError as e:
    e.args[0] == "'tuple' object does not support item assignment"
else:
    raise Exception
