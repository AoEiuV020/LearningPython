#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class CA:
    def __init__(self):
        self.n = 0
    def fca(self):
        self.n += 1

class CB(CA):
    def fca(self):
        super().fca()
        self.n += 2

b = CB()
b.fca()
assert b.n == 3
super(CB, b).fca()
assert b.n == 4
