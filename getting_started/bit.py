#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert 0b10101100 & 0b11001010 == 0b10001000
assert 0b10101100 | 0b11001010 == 0b11101110
assert 0b10101100 ^ 0b11001010 == 0b01100110

# 反直觉，python整数没有最高位符号位，
n = 0b1010
assert ~n != n ^0b1111
assert ~n == -(n) - 1
assert bin(10) == '0b1010'
assert bin(~10) == bin(-11) == '-0b1011'
