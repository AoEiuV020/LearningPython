#!/usr/bin/env python3
# -*- coding: utf-8 -*-

assert len('asdf') == 4
assert len('asdf\n') == 5
assert len(r'asdf\n') == 6
assert len(r'\'') == 2

assert 'a"s"d' == "a\"s\"d"
assert """
asdf
""" == '\nasdf\n'
assert """\
asdf
""" == 'asdf\n'

assert 'as''df' == 'asdf'
assert 'as' 'df' == 'asdf'
assert ('as''df') == 'asdf'
assert ('as'
        'df') == 'asdf'
s = 'as'
try:
    exec("s 'df'")
except SyntaxError as e:
    assert e.args[0] == 'invalid syntax'
assert s + 'df' == 'asdf'

assert 'asdf'[0] == 'a'
assert 'asdf'[-1] == 'f'
assert 'asdf'[1:-1] == 'sd'
assert 'asdf'[1:-0] == ''
assert 'asdf'[0:-0] == ''
assert 'asdf'[1:] == 'sdf'
assert 'asdf'[-2:] == 'df'
assert 'asdf'[:2] == 'as'
assert 'asdf'[:-1] == 'asd'
try:
    'asdf'[5]
    raise Exceptin
except IndexError as e:
    assert e.args[0] == 'string index out of range'

try:
    s = 'asdf'
    s[0] = 'z'
except TypeError as e:
    assert e.args[0] == "'str' object does not support item assignment"

assert 'a'.rjust(4) == '   a'
assert 'a'.zfill(4) == '000a'

assert '{0}, {1}'.format('a', 'b') == 'a, b'
assert '{}, {}'.format('a', 'b') == 'a, b'
assert '{1}, {0}'.format('a', 'b') == 'b, a'
assert '{a}, {b}'.format(a = 'a', b = 'b') == 'a, b'
assert '{0}, {b}'.format('a', b = 'b') == 'a, b'
assert '{0:.2f}'.format(0.1234) == '0.12'
assert '{0:4.1f}'.format(0.1234) == ' 0.1'
assert '{0:04.1f}'.format(0.1234) == '00.1'
assert '{0:4d}'.format(8) == '   8'
assert '{0:4d}'.format(-8) == '  -8'
assert '{:4d}'.format(-8) == '  -8'
assert '{0:04d}'.format(-8) == '-008'
assert '{:4}'.format('a') == 'a   '

zh = '中文'
assert '{!a}'.format(zh) == "'\\u4e2d\\u6587'"
assert eval('{!a}'.format(zh)) == zh
assert '{!a}'.format(zh) != repr(zh)
assert '{0!a}'.format(zh) == '{!a}'.format(zh)
s = repr(repr(repr(repr(zh))))
assert f'{s}' == s
assert '{!s}'.format(s) == s
assert '{!r}'.format(s) == repr(s)

m = {'age': 22}
assert '{[age]}'.format(m) == str(m['age'])
assert '{[age]:d}'.format(m) == str(int(m['age']))
assert '{[age]:f}'.format(m) != str(float(m['age']))
assert '{[age]:f}'.format(m) == '{:f}'.format(m['age'])
assert '{[age]:f}'.format(m) == '{[age]:.6f}'.format(m)
assert '{age:04d}'.format(**m) == '{:04d}'.format(m['age'])

assert 'a%ss' % 'd' == 'ads'
assert 'a%ds' % 3 == 'a3s'
assert 'a%s%ds' % ('d', 3) == 'ad3s'

assert 's' in 'asdf'

s = 'AoEiuV020'
assert s.lower() == 'aoeiuv020'
assert s.upper() == 'AOEIUV020'
assert isinstance(s[0], str)
assert s[0].lower() == 'a'

assert ' a '.strip() == 'a'

assert '中文'.encode() == b'\xe4\xb8\xad\xe6\x96\x87'
assert '中文'.encode() == bytes('中文', 'utf8')
assert '中文'.encode() == bytearray(bytes('中文', 'utf8'))
assert '中文'.encode() == bytearray('中文', 'utf8')

assert 'asdf'.isalpha()
assert '1234'.isdigit()
assert '020'.isdecimal()

# 几个奇怪的方法，不要乱用，
# isdecimal 只接收 0 - 9,
assert '²'.isdigit()
assert not '²'.isdecimal()
assert '²'.isnumeric()
assert not '¼'.isdigit()
assert not '¼'.isdecimal()
assert '¼'.isnumeric()

assert 'a'[0][0][0] is 'a'

assert 'a' < 'b'
