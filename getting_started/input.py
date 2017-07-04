#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from print import Matcher

class Provider:
    def __init__(self, s):
        self.s = s
    def readline(self):
        return self.s

stdin = sys.stdin
stdout = sys.stdout

sys.stdin = Provider('asdf\n')
s = input()
assert s == 'asdf'
sys.stdin = Provider(' asdf \n')
sys.stdout = Matcher('prompt', flashable = True)
s = input('prompt')
assert s == ' asdf '
