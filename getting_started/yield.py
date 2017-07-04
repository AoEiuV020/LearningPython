#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo(s):
    for c in s:
        yield int(c)
g = foo('01234')
assert str(type(g)) == "<class 'generator'>"
assert list(g) == list(range(5))
