#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lam = lambda x: x + 1
assert lam(8) == 9
def foo():
    pass
assert type(lam) == type(foo)

lam = lambda x: (
        x + 1,
        x *2
        )[-1]
assert lam(8) == 16
