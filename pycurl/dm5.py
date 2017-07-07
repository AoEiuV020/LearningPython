#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pycurl
from io import BytesIO
from urllib.parse import urlencode

buf = BytesIO()
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
url = 'http://www.dm5.com/chapterfun.ashx'

# 一样的慢，一定是哪里有问题，
# 只要挂代理，就算是抓包用的本地代理，都能正常速度，
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.POSTFIELDS, urlencode(data))
c.setopt(c.WRITEDATA, buf)
c.setopt(c.VERBOSE, False)
c.setopt(c.PROXY, proxies['http'])
c.setopt(c.USERAGENT, headers['User-Agent'])
c.setopt(c.REFERER, headers['Referer'])
c.perform()
c.close()

print(buf.getvalue().decode('utf-8').strip())
