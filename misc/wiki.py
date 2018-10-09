#!/usr/bin/python3
import pdfkit,sys
if len(sys.argv) < 2:
	print('give a search key')
	sys.exit()
key=sys.argv[1]
pdfkit.from_url('https://en.wikipedia.org/wiki/'+key, key+'.pdf') 
