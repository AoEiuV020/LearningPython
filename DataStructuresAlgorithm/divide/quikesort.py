#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
快排,
用某个值分list成大小两半，
"""
import random

def test(quick):
    l = random.sample(range(99), 10)
    s = sorted(l)
    quick(l)
    assert l == s

def _swap(l, a, b):
    l[a], l[b] = l[b], l[a]
def _part(l, a, b):
    j = random.randrange(a, b)
    _swap(l, a, j)
    i = a + 1
    j = b - 1
    while i < j:
        while i < len(l) and l[i] < l[a]:
            i += 1
        while j >= 0 and l[j] > l[a]:
            j -= 1
        if i < j:
            _swap(l, i, j)
    if l[a] > l[j]:
        _swap(l, a, j)
    return j
def _quick(l, a, b):
    if b - a <= 1:
        return
    m = _part(l, a, b)
    _quick(l, a, m)
    _quick(l, m + 1, b)
    
def quick(l):
    _quick(l, 0, len(l))
test(quick)
