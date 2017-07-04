#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 static,
"""

class C:
    @classmethod
    def f(cls):
        assert cls == C

C.f()

