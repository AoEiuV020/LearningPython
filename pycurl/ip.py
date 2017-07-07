#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pycurl
from io import BytesIO

buf = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://ip.cip.cc')
c.setopt(c.WRITEDATA, buf)
#c.setopt(c.VERBOSE, True)
c.setopt(c.USERAGENT, 'libcurl')
c.perform()
c.close()

print(buf.getvalue().decode('utf-8').strip())
