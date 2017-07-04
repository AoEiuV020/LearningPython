#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
"""
assert max(2, 8) == 8
assert list(map(max, [1, 2], [0], [-1])) == [1]
