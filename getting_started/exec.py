#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 正常执行，但是没有返回值，

try:
    exec('assert False')
    raise Exception
except AssertionError:
    pass

exec('a = 3')
assert a == 3

e = exec('8')
assert type(e) == type(None)

g = {}
l = {}
exec('global a; a, b = 1, 2', g, l)
assert g['a'] == 1
assert l['b'] == 2

import sys

from input import Provider
from print import Matcher

sys.stdin = Provider('2 2\n')
sys.stdout = Matcher('4\n', flashable=True)
exec(open('exec_test_script').read())
sys.stdin = Provider('4 4\n')
sys.stdout = Matcher('256\n', flashable=True)
exec(open('exec_test_script').read())
