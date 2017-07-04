#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
"""

assert list(map(lambda x: x * x, range(3))) == [0, 1, 4]
assert ''.join(list(map(lambda x: str(x), range(3)))) == '012'
assert list(map(int, range(8))) == list(range(8))

try:
    list(map(int, range(3), range(3, 6)))
except TypeError as e:
    assert e.args[0] == "int() can't convert non-string with explicit base"
else:
    raise Exception
assert list(map(lambda x, y: x + y, range(3), range(3, 6))) == [0 + 3, 1 + 4, 2 + 5]
# 取最短，
assert list(map(lambda x, y: x + y, range(3), range(3, 9))) == [0 + 3, 1 + 4, 2 + 5]
