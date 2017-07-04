#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert int('89') == 89
assert int('101', 2) == 5
assert int('0B101', 2) == 5
assert int('27', 8) == 23
assert int('027', 8) == 23
assert int('22', 16) == 34
assert int('0x22', 16) == 34
assert int('0X22', 16) == 34
