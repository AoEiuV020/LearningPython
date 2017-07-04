#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class C:
    def __init__(self):
        self.b = 0
    a = 0

c = C()
assert c.a == 0
assert c.b == 0

assert 'a' in dir(c)
assert 'b' in dir(c)
delattr(c, 'b')
assert not 'b' in dir(c)
try:
    delattr(c, 'a')
except AttributeError as e:
    assert e.args[0] == "a"
else:
    raise Exception
