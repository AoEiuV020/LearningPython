#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert issubclass(int, int)
assert not issubclass(int, float)
assert issubclass(int, (int, float))

class CA:
    pass
class CB(CA):
    pass

assert issubclass(CB, CA)
