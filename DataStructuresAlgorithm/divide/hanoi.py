#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
汉诺塔，移动次数，
hanoi(n) = hanoi(n - 1) * 2 + 1
"""

def test(hanoi):
    assert hanoi(1) == 1
    assert hanoi(2) == 3
    assert hanoi(3) == 7

def hanoi(n):
    if n < 2:
        return 1
    return hanoi(n - 1) * 2 + 1
test(hanoi)
