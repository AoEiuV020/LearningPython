#!/usr/bin/env python3
# -*- coding: utf-8 -*-

flag = True
if flag:
    pass
else:
    raise Exception

if not flag:
    raise Exception
else:
    pass

i = 8
if i > 10:
    raise Exception
elif i > 5:
    pass
else:
    raise Exception
