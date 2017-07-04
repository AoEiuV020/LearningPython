#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tempfile

s = tempfile.NamedTemporaryFile()
with open(s.name, "w") as f:
    f.write('asdf')
    f.flush()
with open(s.name) as f:
    assert f.readline() == 'asdf'
s.close()
