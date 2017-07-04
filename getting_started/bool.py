#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert not bool(None)

assert bool(8)
assert not bool(0)

assert bool('a')
assert not bool('')

assert bool([0])
assert not bool([])

assert bool({0})
assert bool({0: 0})
assert not bool({})

assert True and True
assert False or True
assert not False
assert True or exec('raise Exception')
assert not (False and exec('raise Exception'))
