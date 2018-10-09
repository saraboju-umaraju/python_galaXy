#!/usr/bin/python3
import requests,bs4
res = requests.get('http://www.bloomberg.com/quote/SPX:IND').text
obj = bs4.BeautifulSoup(res,"html.parser")
print(obj.title)
name = obj.find('h1', attrs={'class':'name'})
print(name.text)
name = obj.find('div', attrs={'class':'price'})
#print(name.text)
print(name.title)
