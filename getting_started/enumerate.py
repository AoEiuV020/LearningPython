#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [3, 4, 5]
for i, it in enumerate(l):
    assert l[i] == it

assert type(enumerate(l)) == enumerate

m = {'a': 0, 's': 1}
for i, (k, v) in enumerate(m.items()):
    assert i == v

assert list(enumerate(range(1, 3))) == [(0, 1), (1, 2)]
