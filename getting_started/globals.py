#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 0
global b
g = globals()
assert type(g) == dict
gk = list(g.keys())
assert list(globals().keys()) == ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'a', 'g', 'gk']
b = 1
assert list(globals().keys()) == ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'a', 'g', 'gk', 'b']
assert len(set(globals())) == len(globals())

def foo():
    e = 0
    global f
    f = 1
assert not 'f' in globals().keys()
assert not 'e' in globals().keys()
foo()
assert 'f' in globals().keys()
assert not 'e' in globals().keys()
    
