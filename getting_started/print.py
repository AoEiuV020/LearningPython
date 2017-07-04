#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Matcher(object):
    def __init__(self, expect, flashable = False):
        self.expect = expect
        self.offset = 0
        self.flashable = flashable

    def write(self, message):
        assert message == self.expect[self.offset:self.offset + len(message)]
        self.offset += len(message)
    def flush(self):
        assert self.flashable

stdout = sys.stdout
sys.stdout = Matcher('asdf\n')
print('asdf')
sys.stdout = Matcher('a s d\n')
print('a s d')
sys.stdout = stdout

print('file', file = Matcher('file\n'))
print('end', end = ',', file = Matcher('end,'))

print('{!a}'.format('中文'), file = Matcher("'\\u4e2d\\u6587'\n"))

print('a', flush = True, file = Matcher('a\n', True))

print(1, 2, 3, sep = '', file = Matcher('123\n'))

