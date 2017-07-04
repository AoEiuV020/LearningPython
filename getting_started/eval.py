#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# eval 执行的语句必须要有返回值，

try:
    exec('eval("assert True")')
    raise Exception
except SyntaxError as e:
    assert e.args[0] == 'invalid syntax'

try:
    exec('eval("a = 3")')
    raise Exception
except SyntaxError as e:
    pass

b = eval('2 ** 3')
assert 8 == b
