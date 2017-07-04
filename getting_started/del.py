#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = 8
assert n == 8
del n
try:
    assert n == 8
except NameError as e:
    assert e.args[0] == "name 'n' is not defined"

l = [1, 2, 3]
del l[:]
assert l == []

class C:
    def __init__(self):
        self.b = 0
    a = 0

c = C()
assert c.a == 0
assert c.b == 0

assert 'a' in dir(c)
assert 'b' in dir(c)
del c.b
assert not 'b' in dir(c)
try:
    del c.b
except AttributeError as e:
    assert e.args[0] == "b"
else:
    raise Exception
try:
    del c.a
except AttributeError as e:
    assert e.args[0] == "a"
else:
    raise Exception
