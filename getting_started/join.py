#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = ['a', 's', 'd']
assert ','.join(l) == 'a,s,d'
try:
    assert ','.join([1, 2, 3]) == '1,2,3'
except TypeError as e:
    assert e.args[0] == "sequence item 0: expected str instance, int found"
else:
    raise Exception
assert ','.join(list(map(lambda i: str(i), [1, 2, 3]))) == '1,2,3'

assert str(['a', 's']) == "['a', 's']"

assert ','.join(str(x) for x in [1, 2, 3]) == '1,2,3'
