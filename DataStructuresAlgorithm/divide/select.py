#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
线性时间选择算法,
选出中值，再分成两半，
问题分成左右两半，
"""
import random

def test(select):
    l = random.sample(range(99), 10)
    i = random.randrange(len(l))
    assert l[select(l, i)] == sorted(l)[i]
    l = random.sample(range(999), 100)
    i = random.randrange(len(l))
    assert l[select(l, i)] == sorted(l)[i]
    c = random.randrange(9999)
    l = random.sample(range(c), c // 2)
    i = random.randrange(len(l))
    assert l[select(l, i)] == sorted(l)[i]

def _swap(l, a, b):
    l[a], l[b] = l[b], l[a]
def _sort(l, a, b):
    l[a:b] = sorted(l[a:b])
def _part(l, a, b):
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
def _select(l, k, a, b):
    b = min(b, len(l))
    n = b - a
    if n <= 5:
        _sort(l, a, b)
        return a + k
    for i in range(n // 5):
        f = a + i * 5 # 每组首个元素，
        _sort(l, f, f + 5)
        _swap(l, a + i, (f + min(f + 5, b)) // 2)
    j = _select(l, (i + 1) // 2, a, a + i + 1)
    _swap(l, a, j)
    m = _part(l, a, b) 
    if k < m - a:
        return _select(l, k, a, m)
    else:
        return _select(l, k - (m - a), m, b)
def select(l, k):
    return _select(l, k, 0, len(l))
test(select)
