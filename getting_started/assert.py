#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert True
try:
    assert False
except AssertionError as e:
    assert len(e.args) == 0
else:
    raise Exception

try:
    assert None
except AssertionError as e:
    assert len(e.args) == 0
else:
    raise Exception
