#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = list(range(4))
i = 0
it = iter(l)
n = next(it, None)
while n != None:
    assert n in l
    i += 1
    n = next(it, None)

it = iter(l)
try:
    i = 0
    while True:
        n = next(it)
        i += 1
        assert n in l
except StopIteration as e:
    assert len(e.args) == 0
else:
    raise Exception
assert n == l[-1]
assert i == 4
