#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

l = [1, 2, 3]
assert json.loads('[1, 2, 3]') == l == json.loads(json.dumps(l))
m = {'a': 1, 'b': 2}
assert json.loads('{"a": 1, "b": 2}') == m
