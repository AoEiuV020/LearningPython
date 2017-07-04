#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert pow(2, 3) is 2 ** 3 is 8
assert type(pow(2, 3)) == int
assert pow(2.5, 2) == 2.5 ** 2 == 6.25
assert type(pow(2.5, 2)) == float

assert pow(8, 9, 10) == 8 ** 9 % 10 == 8
try:
    pow(1.1, 2, 3)
except TypeError as e:
    e.args[0] == "pow() 3rd argument not allowed unless all arguments are integers"
else:
    raise Exception
