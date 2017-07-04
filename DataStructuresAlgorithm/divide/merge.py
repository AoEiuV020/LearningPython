#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
合并排序,
分成两半再插入排序，
有一半是事先排好的，另一半插进来就好，
"""
import random

def test(merge):
    l = random.sample(range(99), 10)
    assert merge(l) == sorted(l)

def merge(l):
    if len(l) <= 1:
        return l
    m = len(l) // 2
    left = merge(l[:m])
    right = merge(l[m:])
    for i in range(len(right)):
        j = 0
        while j < len(left):
            if left[j] >= right[i]:
                break
            j += 1
        left.insert(j, right[i])
    return left
test(merge)
