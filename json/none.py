#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

m = {}
m[None] = None
assert json.dumps(m) == '{"null": null}'
assert json.loads(json.dumps(m)) == {'null': None} != m
