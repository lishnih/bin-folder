#!/usr/bin/env python
# coding=utf-8
# Stan 2012-09-06

import urllib2

myurl = 'http://localhost/php/info.php'
try:
    page = urllib2.urlopen(myurl)

    head = page.info().headers
    for i in head:
        print i,

    print

    html = page.readlines()
    for i in html:
        print i,

except Exception, e:
    print e
