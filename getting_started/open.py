#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
open mode rwb+ 和c语言一样，
"""
import tempfile

s = tempfile.NamedTemporaryFile()
f = open(s.name, "w")
f.write('asdf')
f.flush()
f.close()
f = open(s.name)
assert f.readline() == 'asdf'
f.close()
s.close()
