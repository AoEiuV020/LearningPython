#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
带时限的作业排序，
"""
import random

def r(n):
    return random.randrange(1, n)
def test(job):
    l = [(100, 2), (10, 1), (15, 2), (27, 1)]
    assert job(l) == 127

def job(l):
    l.sort(key = lambda x: x[0], reverse = True)
    s = set()
    v = 0
    for i in range(len(l)):
        flag = False
        for j in range(l[i][1], 0, -1):
            if j in s:
                continue
            else:
                flag = True
                s.add(j)
                break
        if flag:
            v += l[i][0]
    return v
test(job)
