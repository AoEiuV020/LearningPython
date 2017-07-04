#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# assert help(print) == None
"""
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
(END)
"""

# https://docs.python.org/3/library/functions.html
"""
abs() all() any() ascii() bin() bool()
bytearray() bytes() callable() chr()
classmethod() compile() complex()
delattr() dict() dir() divmod() enumerate()
eval() exec() filter() float() format()
frozenset() getattr() globals() hasattr()
hash() help() hex() id() __import__()
input() int() isinstance() issubclass()
iter() len() list() locals() map() max()
memoryview() min() next() object() oct()
open() ord() pow() print() property() range()
repr() reversed() round() set() setattr()
slice() sorted() staticmethod() str() sum()
super() tuple() type() vars() zip()
"""

assert str(type(help)) == "<class '_sitebuiltins._Helper'>"
