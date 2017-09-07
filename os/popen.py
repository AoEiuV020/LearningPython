#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

f = os.popen('echo hello')
assert f.readlines()[0] == 'hello\n'
