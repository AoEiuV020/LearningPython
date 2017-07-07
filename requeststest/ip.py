#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('http://ip.cip.cc')
print(r.text.strip())
