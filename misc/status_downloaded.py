#!/usr/bin/python3
import requests

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
	res.raise_for_status()

except Exception as umas:
	print('there was some problem %s' % umas)

