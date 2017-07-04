#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
id和is完全对应，
"""
assert type(id(8)) == int
assert id(8) == id(8)
d = 8.8
assert id(d) == id(8.8)
assert d is 8.8
assert id(d) != id(8 + 0.8)
assert not d is 8 + 0.8
