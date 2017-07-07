#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

l = [1, 2, 3]
assert json.dumps(l) == '[1, 2, 3]' == str(l)
m = {'a': 1, 'b': 2}
assert json.dumps(m) == '{"a": 1, "b": 2}' != str(m)
