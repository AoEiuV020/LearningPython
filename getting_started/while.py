#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [0, 1, 2, 3]
i = 0
while i < len(l):
    assert l[i] == i
    i += 1
assert i == len(l)
