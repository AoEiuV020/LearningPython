#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo():
    pass
assert (foo.__annotations__) == {}
def foo1(age: int, name: str) -> None:
    pass
assert (foo1.__annotations__) == {'age': int, 'name': str, 'return': None}
# 反直觉，就算声明了类型，还是不会检查，
foo1('a', 's')
