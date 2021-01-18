#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class bytearray(object)
 |  bytearray(iterable_of_ints) -> bytearray
 |  bytearray(string, encoding[, errors]) -> bytearray
 |  bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
 |  bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
 |  bytearray() -> empty bytes array
 |  
 |  Construct a mutable bytearray object from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - a bytes or a buffer object
 |    - any object implementing the buffer API.
 |    - an integer
"""

s = '中文'
assert bytearray(s, 'utf-8') == \
       bytearray(bytes(s, 'utf8'))
assert bytearray(s, 'utf-8') == \
       (bytes(s, 'utf8'))
assert len(bytearray(88)) == 88
assert len(bytearray(range(88))) == 88
assert bytearray(9999).__sizeof__() - \
       bytearray(88).__sizeof__() == 9999 - 88

assert bytearray([255])[0] == 255
try:
    bytearray([256])
except ValueError as e:
    assert e.args[0] == "byte must be in range(0, 256)"
else:
    raise Exception

b = bytearray('asdf', 'ascii')
b[0] += 1
assert b[0] == ord('b')
