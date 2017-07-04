#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
求最大,
分两半求最大，
max(l) == max(max(l[:len(l)//2], max(l[len(l)//2:]))
"""
import random

def test(ma):
    l = random.sample(range(99), 10)
    assert ma(*l) == max(l)

def ma(*a):
    if len(a) == 1:
        return a[0]
    m = len(a) // 2
    x = ma(*a[:m])
    y = ma(*a[m:])
    if x > y:
        return x
    else:
        return y
test(ma)
