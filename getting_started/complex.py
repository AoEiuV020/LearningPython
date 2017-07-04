#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert type(0j) == complex
assert str(8j) == '8j'
assert str(1 + 8j) == str(8j + 1) == '(1+8j)'
assert 8j + 1 + 1j == 1 + 9j
assert not 8j + 1 + 1j is 1 + 9j

try:
    int(8j)
except TypeError as e:
    assert e.args[0] == "can't convert complex to int"
else:
    raise Exception
