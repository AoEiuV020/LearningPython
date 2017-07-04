#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = list('sk83n')
assert sorted(l) == list('38kns')
assert sorted(l, reverse = True) == list('snk83')
l.sort()
assert l == list('38kns')
