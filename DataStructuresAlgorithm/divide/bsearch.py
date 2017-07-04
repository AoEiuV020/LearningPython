#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
对半搜索,
"""
import random

def test(search):
    l = sorted(random.sample(range(99), 10))
    i = random.randrange(len(l))
    assert search(l, l[i]) == i
    assert search(l, 999) == None

def _bsearch(l, x, a, b):
    if a >= b:
        return None
    m = (a + b) // 2
    if (x < l[m]):
        return _bsearch(l, x, a, m)
    elif (x > l[m]):
        return _bsearch(l, x, m + 1, b)
    else:
        return m
def bsearch(l, x):
    return _bsearch(l, x, 0, len(l))
test(bsearch)

def _bsearch1(l, x, a, b):
    """
    感觉这样一半一半的才对应判定二叉树，
    """
    if a >= b:
        return None
    m = (a + b) // 2
    if (x < l[m]):
        return _bsearch(l, x, a, m)
    elif (x > l[m]):
        return _bsearch(l, x, m, b)
def bsearch1(l, x):
    return _bsearch(l, x, 0, len(l))
test(bsearch1)
