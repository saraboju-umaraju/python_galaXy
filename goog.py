#!/usr/bin/python3

import urllib.request

#try:
	#x=urllib.request.urlopen('https://www.google.com/search?q=test')
#	print(x.read())
#except Exception as e:
#	print(e)

try:
	url='https://www.google.com/search?q=test'

	headers={}
	headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
	req = urllib.request.Request('https://www.google.com/search?q=test',headers=headers)
	resp=urllib.request.urlopen(req)
	respdata=resp.read()
	
except Exception as e:
	print(e)
