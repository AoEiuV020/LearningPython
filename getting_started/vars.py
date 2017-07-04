#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert vars() == locals()
class CA:
    pass
a = CA()
assert vars(a) == a.__dict__

try:
    vars(8)
except TypeError as e:
    e.args[0] == "vars() argument must have __dict__ attribute"
else:
    raise Exception
