#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert __name__ == '__main__'

def foo():
    assert __name__ == '__main__'
foo()

class C:
    def bar(self):
        assert __name__ == '__main__'
C().bar()

import module
assert module.__name__ == 'module'
