#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument.
"""

assert min(8, 2) == 2
assert min(range(8)) == 0
