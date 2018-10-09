#!/usr/bin/python3
import bs4,requests
#res = requests.get('http://lwn.net/Articles/204545/')
#soup=bs4.BeautifulSoup(res.content,'html.parser')
#print(soup.body.text)
import pdfkit
pdfkit.from_url('http://lwn.net/Articles/204545/','out.pdf')
