#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
阶乘,
n! 分成 n 和 (n - 1)!
"""
def test(fact):
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(4) == 2 * 3 * 4 == 24

def fact(n):
    if n < 2:
        return 1
    t = 1
    for i in range(2, n + 1):
        t *= i
    return t
test(fact)

def rfact(n):
    if n < 2:
        return 1
    return n * rfact(n - 1)
test(rfact)
