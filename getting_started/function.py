#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i = 0
def foo(it):
    it += 1
assert str(type(foo)) == "<class 'function'>"
assert i == 0
foo(i)
assert i == 0

def bar(*args):
    assert len(args) == 3
    assert type(args) == tuple
    assert list(args) == [1, 2, 3]
bar(1, 2, 3)

def fun(*args, **kwargs):
    assert len(kwargs) == 2
    assert type(kwargs) == dict
    assert kwargs == {'a': 1, 's': '2'}
    try:
        assert kwargs['d'] == 3
    except KeyError:
        pass
    else:
        raise Exception
fun(a = 1, s = '2')

def inc(i):
    return i + 1
assert inc(8) == 9

i = 1
def fooi(arg = i):
    assert arg == 1
fooi()
i = 0
fooi()

# 又是个反直觉的，默认参数是复用的，
class wrapper:
    i = 0
def foolist(it, arg = [], i = wrapper()):
    assert it == len(arg) == i.i
    arg.append(it)
    i.i += 1
foolist(0)
foolist(1)
foolist(2)
def foolistn(it, arg = None):
    if arg == None:
        arg = []
    arg.append(it)
    assert arg == [it]
foolistn(0)
foolistn(1)
foolistn(2)

def fooarg(a = 'a', b = 'b'):
    pass
try:
    exec("fooarg(a = 'a', 'b')")
except SyntaxError as e:
    assert e.args[0] == "positional argument follows keyword argument"
else:
    raise Exception

try:
    fooarg('a', a = 'a')
except TypeError as e:
    assert e.args[0] == "fooarg() got multiple values for argument 'a'"
else:
    raise Exception

try:
    exec("def fooarg(a = 'a', b, c = 'c'):\n  pass")
except SyntaxError as e:
    assert e.args[0] == "non-default argument follows default argument"
else:
    raise Exception
