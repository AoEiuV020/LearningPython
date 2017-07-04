#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [1, 2, 3, 4]
i = 0
it = iter(l)
while True:
    try:
        n = next(it)
    except StopIteration as e:
        assert len(e.args) == 0
        break
    assert n == l[i]
    i += 1
assert i == 4
assert n == l[-1]

i = 0
it = iter(l)
while True:
    n = next(it, None)
    if (n == None):
       break
    assert n == l[i]
    i += 1
assert i == 4
assert n == None
