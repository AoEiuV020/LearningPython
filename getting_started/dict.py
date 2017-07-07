#!/usr/bin/env python3
# -*- coding: utf-8 -*-

m = {'a': 1, 's': '2'}
assert m['a'] == 1
assert m['s'] == '2'
assert len(m) == 2

m = dict([(1, 2), (3, 4)])
assert m == {1: 2, 3: 4}
assert 1 in m
assert not 2 in m
assert (1, 2) in m.items()
assert 2 in m.values()

for k, v in m.items():
    assert v == m[k]

assert str(type(m.items())) == "<class 'dict_items'>"
assert str(type(m.keys())) == "<class 'dict_keys'>"
assert str(type(m.values())) == "<class 'dict_values'>"

assert list(m) == list(m.keys())
m = {'a': 1, 's': '2'}
l = []
for k in m:
    l.append(m[k])
assert l == [1, '2']
assert l == list(m.values())

assert str(type(m.__iter__())) == "<class 'dict_keyiterator'>"
assert str(type(iter(m))) == "<class 'dict_keyiterator'>"

def foo(*args, sep, end, file):
    assert list(args) == [1, 2, 3, 4]
    assert sep == ''
    assert end == ''
    assert file == 'fff'
kwargs = {'sep' : '', 'end' : '', 'file' : 'fff'}
foo(1, 2, 3, 4, **kwargs)

m = {}
try:
    m['c']
except KeyError as e:
    e.args[0] == "'c'"
else:
    raise Exception
assert m.get('c') == None
assert not 'c' in m.keys()
m['c'] = None
assert 'c' in m.keys()
assert m['c'] == None
assert m.get('c') == None
