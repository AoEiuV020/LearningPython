#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert ascii('中文') == "'\\u4e2d\\u6587'"
assert ascii([]) == '[]'
# 自带repr的效果，
assert ascii('asdf') == "'asdf'"
