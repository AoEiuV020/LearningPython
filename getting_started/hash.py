#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
反直觉，is 和 hash 没什么关系，
"""
assert hash(1.00 + 0.01) == hash(1.01)
assert id(1.00 + 0.01) != id(1.01)
assert 1.00 + 0.01 == 1.01
assert not 1.00 + 0.01 is 1.01

assert type(hash('s')) == int
