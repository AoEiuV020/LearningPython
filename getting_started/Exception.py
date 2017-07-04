#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    n
    raise Exception
except NameError as e:
    assert type(e) == NameError
    assert len(e.args) == 1
    assert type(e.args) == tuple
    assert e.args[0] == "name 'n' is not defined"

try:
    raise Exception('a', 'b')
except Exception as e:
    assert type(e) == Exception
    assert len(e.args) == 2
    assert e.args[0] == 'a'
    assert e.args[1] == 'b'
finally:
    pass

try:
    raise Exception
except:
    pass
else:
    raise Exception

a = 0
try:
    pass
except Exception:
    raise Exception
else:
    a = 1
assert a == 1

try:
    try:
        raise Exception('a')
    except Exception as e:
        raise Exception('b') from e
except Exception as e:
    assert e.__cause__.args[0] == 'a'
    assert e.args[0] == 'b'
