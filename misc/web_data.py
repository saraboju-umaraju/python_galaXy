#!/usr/bin/python3
import urllib.request
#http://www.news18.com/cricketnext/live-commentary/new-zealand-in-india-3-test-series-2016/india-vs-new-zealand/innz10082016181602.html
downloaded_data  = urllib.request.urlopen('http://www.news18.com/cricketnext/live-commentary/new-zealand-in-india-3-test-series-2016/india-vs-new-zealand/innz10082016181602.html')
for line in downloaded_data.readlines():
    print(str(line))
