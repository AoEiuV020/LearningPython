#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
callable(obj, /)
    Return whether the object is callable (i.e., some kind of function).
    
    Note that classes are callable, as are instances of classes with a
    __call__() method.
"""
assert callable(list)
assert callable(abs)
assert not callable(8)

class C:
    pass
assert callable(C)
