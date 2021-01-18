#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [1, 2, 3, 4]
assert type(l) == list
assert len(l) == 4
assert l[1] == 2
l[1] = 5
assert l[1] == 5
assert len(l[1:-1]) == 2


# [:]深拷贝，反常识，
# 修改[:]的元素不会作用到原list,
# 直接给[:]赋值会作用到原list，当成特殊情况吧，
# 间接给[:]赋值不会作用到原list，
# 直接给[:][:]赋值不会作用到原list,

l = [1, 2, 3, 4]
l[:][1] = 6
assert l[1] == 2

l = [1, 2, 3, 4]
tmp_l = l[:]
assert len(tmp_l) == 4
assert not tmp_l[:] is tmp_l
tmp_l[:] = []
assert len(tmp_l) == 0
assert len(l) == 4

l = [1, 2, 3, 4]
tmp_l = l[:]
assert len(tmp_l) == 4
tmp_l = []
assert len(tmp_l) == 0
assert len(l) == 4

l = [1, 2, 3, 4]
tmp_l = l[:]
assert len(tmp_l) == 4
tmp_l[:][:] = []
assert len(tmp_l) == 4
assert len(l) == 4


try:
    l = [1, 2, 3, 4]
    l[8]
    raise Exception
except IndexError as e:
    e.args[0] == 'IndexError: list index out of range'

l = [1, 'a']
assert type(l[0]) == int
assert type(l[1]) == str

l = [1, 2]
l.append(3)
assert l == [1, 2, 3]
l.insert(0, 9)
assert l == [9, 1, 2, 3]
l[len(l):] = [8]
assert l == [9, 1, 2, 3, 8]

assert str(type(l.__iter__())) == "<class 'list_iterator'>"
assert str(type(iter(l))) == "<class 'list_iterator'>"

assert list(range(3)) == [0, 1, 2]

assert 1 in [0, 1, 2]

assert [i for i in range(3)] == [0, 1, 2]

assert list((0, 1, 2, 3, 4)) == list(range(5))

def com(a):
    return a * a
l = list(range(4, -4, -1))
l.sort(key = com)
assert l == [0, 1, -1, 2, -2, 3, -3, 4]
l.sort(key = lambda x: -x)
assert l == list(range(4, -4, -1))
l.sort(key = lambda x: -x, reverse = True)
assert l == list(range(-3, 5, 1))

l = [1, 2]
l.extend(iter(l[:]))
assert l == [1, 2, 1, 2]
l = [1, 2]
l[len(l):] = (iter(l[:]))
assert l == [1, 2, 1, 2]

# 反直觉，remove不是删除指定下标，
l = [3, 4]
l.remove(3)
assert l == [4]
l = [3, 4]
l.pop(1)
assert l == [3]
l = [3, 4]
l[:1] = []
assert l == [4]

l = [1, 2]
assert l.reverse() == None
assert l == [2, 1]

assert not l is l.copy()
l = [1, 2]
try:
    exec('l.copy() = []')
except SyntaxError as e:
    assert e.args[0] == "can't assign to function call"
else:
    raise Exception

l = [1, 2, 2, 3]
assert l.count(2) == 2
assert l.index(2) == 1
assert l.index(2, 2) == 2
try:
    l.index(3, 0, 2)
except ValueError as e:
    e.args[0] == "3 is not in list"
else:
    raise Exception

# 反直觉，这个pop不是对应push，而是按索引remove,
l = [1, 2, 3, 4]
assert l.pop() == 4
assert l == [1, 2, 3]
assert l.pop(0) == 1
assert l == [2, 3]

l == [1, 2, 3]
del l[:]
assert l == []

l = list(range(9))
assert l[3:8:2] == [3, 5, 7]
l[3:8:2] = [1, 2, 3]
assert l == [0, 1, 2, 1, 4, 2, 6, 3, 8]
try:
    l[3:8:2] = []
except ValueError as e:
    e.args[0] == "attempt to assign sequence of size 0 to extended slice of size 3"
else:
    raise Exception
