#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
看起来是比较底层的东西，不知道用在哪，
"""
assert memoryview(bytes([1])) != None
try:
    memoryview(8)
except TypeError as e:
    e.args[0] == "memoryview: a bytes-like object is required, not 'int'"
else:
    raise Exception

b = bytes(list(range(8)))
assert bytes(memoryview(b)) == b

b = bytearray('1234', 'ascii')
m = memoryview(b)
assert m[0] == ord('1')
m[0] += 1
assert m[0] == ord('2')
