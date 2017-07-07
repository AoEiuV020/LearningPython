#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

data = {}
data['cid'] = 497816
data['page'] = '1'
data['key'] = ''
data['language'] = '1'
data['gtk'] = '6'
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
headers['Referer'] = 'http://www.dm5.com/'
proxies = {'http': 'http://localhost:8080'}
proxies = {}

# 和urllib一样诡异的慢，
r = requests.post('http://www.dm5.com/chapterfun.ashx', data = data, headers = headers, proxies = proxies)
print(r.text)
# 第二次快些，还是慢的不正常，
r = requests.post('http://www.dm5.com/chapterfun.ashx', data = data, headers = headers, proxies = proxies)
print(r.text)
