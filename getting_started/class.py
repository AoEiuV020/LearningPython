#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class C:
    i = 0

    def get_i(self):
        return self.i


c = C()
assert c.i == 0
c.i = 1
assert c.i == 1
assert c.i == c.get_i()

# 下面定义的类不可见，
try:
    D()
except NameError as e:
    assert e.args[0] == "name 'D' is not defined"


class D:
    pass
