#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert str(chr(8)) == '\x08'
assert str(chr(888)) == '\u0378'
assert str(chr(88888)) == '\U00015b38'

assert chr(88) is 'X'
assert chr(bytes('X', 'ascii')[0]) == 'X'
assert chr(ord('中')) == '中'
