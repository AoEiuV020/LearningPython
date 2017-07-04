#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
辗转相除法，
不考虑负数，
"""
def test(gcd):
    assert gcd(3, 9) == 3
    assert gcd(12, 23) == 1
    assert gcd(18, 81) == 9
    assert gcd(7, 0) == 7
    assert gcd(0, 7) == 7

def gcd(m, n):
    if m == 0:
        return n
    while n % m > 0:
        m, n = n % m, m
    return m
test(gcd)

def rgcd(m, n):
    if m == 0:
        return n
    if n % m == 0:
        return m
    else:
        return rgcd(n % m, m)
test(rgcd)

def egcd(m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    t = min(m, n)
    while m % t or n % t:
        t -= 1
    return t
test(egcd)

def egcd2(m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    for t in range(min(m, n), 0, -1):
        if m % t == 0 and n % t == 0:
            return t
test(egcd2)

