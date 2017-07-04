#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
斐波那契数列,
fib(n) 分成 fib(n - 1), fib(n - 2) 
"""

def test(fib):
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
test(fib)
