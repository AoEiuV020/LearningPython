#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert type(8) == int
assert type(8.8) == float
assert 8 is 2 ** 3
assert 4 ** 0.5 == 2.0
assert 8 ** -1 == 1 / 8
assert 0.5 == 1 / 2
assert type(1 / 2) == float
assert 0 is 1 // 2
assert type(1 // 2) == int
assert -1 is -1 // 2 # 下取整，反常识，但和 int(-1 // 2) 区分开了，
assert 1 + 2 * 3 ** 4 == 1 + (2 * 3 ** 4) == 1 + (2 * (3 ** 4))
assert -1 + -2 * -3 ** -4 == -1 + (-2 * -3 ** -4) == -1 + (-2 * -(3 ** -4))
assert -2 ** 2 == -(2 ** 2) == -4
assert (-2) ** 2 == 4
assert 1.23574 == 1.1 * 1.1234
assert 1.2357400000000001 == 1.1 * 1.1234
assert not 1.2357400000000001 is 1.1 * 1.1234
assert 1.235740000000001 != 1.1 * 1.1234
assert not 2.0 + 0 is 2.0
assert 2.0 + 0 == 2.0

# 没有++/--, 只是+无视，-取反，
i = 1
assert -i == -1
assert --i == 1
assert ---i == -1
assert +i == 1
assert ++i == 1
assert ++++++i == 1

assert 1.0 == 1
assert '1' != 1

assert int(1.1) == 1
assert type(int(1.1)) == int
assert int(8.8) == 8
assert int(-8.8) == -8
assert type(str(1.1)) == str
assert str(1.1) == '1.1'

try:
    1 / 0
except ZeroDivisionError as e:
    e.args[0] == "division by zero"
else:
    raise Exception
try:
    1.0 / 0
except ZeroDivisionError as e:
    e.args[0] == "float division by zero"
else:
    raise Exception

# 反直觉，八进制字面值开头是0o，零欧，
assert 0b10101010 == 0xaa == 0xAA == 0Xaa == 0XAA == 0o252 == 0O252
