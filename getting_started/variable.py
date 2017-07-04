#!/usr/bin/env python3
# -*- coding: utf-8 -*-
w = 2
h = 3
assert 6 == w * h

# _ 在命令行交互式repl有效，代表上一行返回值，
try:
    _
except NameError as e:
    assert e.args[0] == "name '_' is not defined"

a, b = 2, 3
assert a == 2
assert b == 3
a, b = a + b, a * b
assert a == 5
assert b == 6
