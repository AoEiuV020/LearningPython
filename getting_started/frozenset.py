#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = list(range(9))
l.append(3)
f = frozenset(l)
assert type(f) == frozenset
assert str(f) == 'frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8})'
assert f == set(range(9))
assert len(f) == 9
