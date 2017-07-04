#!/usr/bin/env python3
# -*- coding: utf-8 -*-

g = (str(i) for i in range(3))
assert next(g) == '0'
assert list(g) == ['1', '2']

g = ((x * y) for x in range(3) for y in range(4))
assert list(g) == [0, 0, 0, 0, 0, 1, 2, 3, 0, 2, 4, 6]

g = (i for i in range(8) if i % 3 == 0)
assert list(g) == [0, 3, 6]

assert [i for i in range(3)] == [0, 1, 2]
