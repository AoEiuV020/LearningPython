#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import asdf
except ImportError:
    pass
else:
    raise Exception

try:
    from .module import C
except ModuleNotFoundError as e:
    assert e.args[0] == "No module named '__main__.module'; '__main__' is not a package"
else:
    raise Exception

import math as m
assert m.pi == 3.141592653589793
