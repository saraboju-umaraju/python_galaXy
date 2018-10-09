#!/usr/bin/python3
#http://webapps.stackexchange.com/questions/58550/what-does-tbm-mean-in-google-search
import webbrowser,requests,bs4
import time,re
import requests
import sys,time
def find_max():
	link='https://www.shutterstock.com/search?&searchterm=ss'
	res = requests.get(link)
	res.raise_for_status()
	res = requests.get(link).text
	soup=bs4.BeautifulSoup(res,'html.parser')

	set=soup.find_all('span',{"class":"page-max"})
	res=re.compile(r"\d\d,\d\d\d|\d,\d\d\d|\d,\d\d|(\d\d)|\d")
	#res=re.compile(r"\d\d|\d{1,2},?\d{2,4}?|\d{1,2},\d{2,4}|\d\d,\d\d\d")
	mo=res.search(str(set))
	print(mo)
	return (str(mo.group())).replace(',','')
print(find_max())
