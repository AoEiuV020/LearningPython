#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = list(range(9))
assert l[slice(3, 8, 2)] == l[3:8:2] == [3, 5, 7]
