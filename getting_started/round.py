#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert 0.123 == round(0.123456, 3)
assert 0 == round(0.123456)

assert type(round(1.2)) == int
assert type(round(1.2, 1)) == float
