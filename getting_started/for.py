#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [1, 2, 3, 4]
i = 1
for it in l:
    assert it == i
    i += 1
assert i == 5
for it in l[:]:
    l.append(-it)
assert l == [1, 2, 3, 4, -1, -2, -3, -4]

m = {'a': 1, 's': '2'}
l = [1, '2']
i = 0
for k in m:
    assert l[i] == m[k]
    i += 1
for k, v in m.items():
    assert v == m[k]
for (k, v) in m.items():
    assert v == m[k]
i = 0
for it in m.items():
    assert l[i] == m[it[0]] == it[1]
    i += 1
for i, (k, v) in enumerate(m.items()):
    assert l[i] == m[k] == v
try:
    for i, k, v in enumerate(m.items()):
        assert l[i] == m[k] == v
except ValueError as e:
    e.args[0] == 'not enough values to unpack (expected 3, got 2)'
else:
    raise Exception
