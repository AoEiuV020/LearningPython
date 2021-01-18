#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

f = os.popen('echo hello')
assert type(f) == os._wrap_close
# 这个readlines方法在dir(f)和help(f)都没有提到，
assert not 'readlines' in dir(f)
l = f.readlines()
assert type(l) == list
