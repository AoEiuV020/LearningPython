#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert type(range(3)) == range
assert range(3) != [0, 1, 2]
assert range(3) == range(0, 3)
l = []
for i in range(3):
    l.append(i)
assert l == [0, 1, 2]
l = []
for i in range(2, 4):
    l.append(i)
assert l == [2, 3]

l = []
for i in range(0, 10, 3):
    l.append(i)
assert l == [0, 3, 6, 9]

assert len(range(0, 1, -1)) == 0

# 反直觉，不要用==,
assert range(0, 10, 3) == range(0, 11, 3)
assert range(0, 0, 1) == range(0, 0, 2)
assert range(0, 9, -1) != range(0, 12, 1)
assert range(0, 0, -1) == range(0, 0, 1)
assert range(0, -1, -2) == range(0, 1, 2)
assert range(0, -1, -2) != range(-1, 0, 2)
assert range(-1, 0, -2) == range(1, 0, 2)
assert range(1, 0, -44) != range(0, 1, 44)

assert type(list(range(3))) == list
assert list(range(3)) == [0, 1, 2]

# O(1)
assert 9 in range(9999999999999999999999999999)
