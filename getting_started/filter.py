#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert list(filter(lambda x: x > 3, range(8))) \
       == list(range(4, 8))

# None 过滤bool(x) == False的情况，
assert list(filter(lambda x: x, range(8))) \
       == list(filter(None, range(8))) \
       == list(range(1, 8))

assert list(filter(lambda x: x.isalpha(), 'AoEiuV020')) \
       == list('AoEiuV')
