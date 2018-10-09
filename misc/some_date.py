#!/usr/bin/python3
import requests,bs4,time
while True:
	lin=requests.get('https://www.timeanddate.com/').text
	obj=bs4.BeautifulSoup(lin,"html.parser")
	some=obj.find('h2',attrs={'class':'t-sq','id':'current'})
	print(some.text)
	date=obj.find('span' ,attrs={'id':'clk_hm'})
	print(date.text,end=' ')
	date=obj.find('span' ,attrs={'id':'ij0'})
	print(date.text)
	time.sleep(3)
