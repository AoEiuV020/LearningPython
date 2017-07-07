#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

with urllib.request.urlopen('http://ip.cip.cc') as f:
    ip = f.readline().decode('ascii').strip()
    print(ip)

