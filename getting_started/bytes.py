#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert type(b'asdf') == bytes
assert len(b'asdf') == 4
assert str(b'asdf') == "b'asdf'"
assert type(b'asdf'[0]) == int
assert b'asdf'[0] == 97
assert len('中文') == 2
assert len(bytes('中文', encoding = 'utf-8')) == 6

try:
    bytes('', 'fe')
except LookupError as e:
    assert e.args[0] == 'unknown encoding: fe'
else:
    raise Exception

b = bytes(3)
assert b[0] == 0
try:
    b[0] = 1
except TypeError as e:
    assert e.args[0] == "'bytes' object does not support item assignment"
else:
    raise Exception

b = bytes('中文', 'utf-8')
assert str(b, 'utf-8') == '中文'
assert b.decode('utf-8') == '中文'

