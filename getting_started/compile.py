#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
大概是事先编译好会运行的更快吧，
中间参数<string>并没有什么限制，只是表明代码出处，
比如报错时会出现，
"""

c = compile('assert False', '<string>', 'exec')
try:
    exec(c)
    raise Exception
except AssertionError:
    pass
try:
    # 这样可以用eval运行无返回值的代码，
    eval(c)
    raise Exception
except AssertionError:
    pass

try:
    c = compile('assert False', '<string>', 'eval')
    raise Exception
except SyntaxError as e:
    assert e.args[0] == 'invalid syntax'

c = compile('2 ** 3', '<string>', 'eval')
e = exec(c)
assert type(e) == type(None)
n = eval(c)
assert n == 8

c = compile('a = 2; a += a; assert a == 4', '<string>', 'single')
exec(c)
assert type(eval(c)) == type(None)
try:
    c = compile('a = 2\n a += a\n assert a == 4', '<string>', 'single')
    raise Exception
except SyntaxError as e:
    assert e.args[0] == 'multiple statements found while compiling a single statement'

