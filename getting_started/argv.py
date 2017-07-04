#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
assert len(sys.argv) > 0
# __file__ 不是当前文件名，而是sys.argv[0]
assert sys.argv[0] == __file__
