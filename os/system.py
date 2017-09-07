#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('../getting_started')
from print import Matcher

sys.stdout = Matcher("python\n", True)
#输出不会到sys.stdout, 还是在控制台输出，
assert 0 == os.system('echo python')
print('python')
