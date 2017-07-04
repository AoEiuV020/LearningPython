#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = set('asdffdsa')
assert type(s) == set
assert s == {'a', 's', 'd', 'f'}
assert type({'a'}) == set

a = set('asd')
b = set('qaz')
assert a - b == set('sd')
assert a | b == set('asdqz')
assert a & b == set('a')
assert a ^ b == set('sdqz')

assert sorted(set('asdf')) == list('adfs')

assert type(set()) == set
assert len(set()) == 0
assert str(set()) == "set()"
assert str(set((1, 2))) == "{1, 2}"
assert {1, 2} == set((1, 2))
try:
    set(1)
except TypeError as e:
    e.args[0] == "'int' object is not iterable"
else:
    raise Exception

s = set(range(4))
try:
    s[0]
except TypeError as e:
    e.args[0] == "'set' object does not support indexing"
else:
    raise Exception
i = 0
for it in s:
    assert it in s
    i += 1
assert i == 4
it = iter(s)
i = 0
n = next(it, None)
while n != None:
    assert n in s
    i += 1
    n = next(it, None)
assert i == 4
