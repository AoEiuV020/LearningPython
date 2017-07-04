#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert locals() == globals()
assert type(locals()) == dict

def foo():
    a = 0
    assert locals() != globals()
    assert 'a' in locals()
    assert not 'a' in globals()
foo()
