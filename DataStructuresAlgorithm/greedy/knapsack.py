#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
背包问题,
排好序再贪心很简单，
"""
import random

def r(n):
    return random.randrange(1, n)
def test(knapsack):
    l = [(25, 18), (24, 15), (15, 10)]
    assert knapsack(l, 20) == (31.5, 20)

def knapsack(l, mw):
    l.sort(key = lambda x: x[0] / x[1], reverse = True)
    s = []
    w = 0
    v = 0
    for i in range(len(l)):
        c = min(l[i][1], mw - w)
        w += c
        v += l[i][0] / l[i][1] * c
    return (v, w)
test(knapsack)
