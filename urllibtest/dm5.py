#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request as req
import urllib.parse as par

data = {}
data['cid'] = 497816
data['page'] = '2'
data['key'] = ''
data['language'] = '1'
data['gtk'] = '6'
data = par.urlencode(data).encode('ascii')
r = req.Request('http://www.dm5.com/chapterfun.ashx', data)
r.set_proxy('localhost:8080', 'http')
r.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36')
r.add_header('Referer', 'http://www.dm5.com/')
# 非常慢，很久才发起请求，每次都是，
# 但加上代理抓包，第一次很久才抓到包，
# 之后请求就快了，
with req.urlopen(r) as f:
    print(f.read().decode('ascii'))
