#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert type(bin(0)) == str
assert bin(7) == '0b111'
assert bin(2 ** 31) == '0b10000000000000000000000000000000'
assert int(bin( 3 ** 10), 2) == 3 ** 10

assert bin(10) == '0b1010'
assert bin(~10) == bin(-11) == '-0b1011'
