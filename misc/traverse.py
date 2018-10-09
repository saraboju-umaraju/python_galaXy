#!/usr/bin/python3
#http://webapps.stackexchange.com/questions/58550/what-does-tbm-mean-in-google-search
import webbrowser,requests,bs4
import time,re
import requests
import sys,time

def find_pass(link):
	res=requests.get(link).text
	print(key)
	soup=bs4.BeautifulSoup(res,'html.parser')
	limit=soup.find('input',{'name':'pagi'}).text
	limit=limit.strip()
	#new=re.compile("\d+|\d{4}+|\d{3}+|\d{2}+|\d{1}+")
	new=re.compile("\d{1,5}")
	mo=new.search(limit)
	print(mo.group())
	return mo.group()

def doimage(link):
        res = requests.get(link)
        res.raise_for_status()
        name=str(time.time())
        image = open(name,'wb')
        for chunk in res.iter_content(100000):
                image.write(chunk)
        image.close()
if len(sys.argv ) < 2:
	key='fuck'
else: 
	key=sys.argv[1]
linked='https://pixabay.com/en/photos/?orientation=&q='+key
for num in range(1,int(find_pass(linked))): 
	link='https://pixabay.com/en/photos/?orientation=&q='+key+'&pagi='+str(num)
	res = requests.get(link)
	print(key)
	res.raise_for_status()
	res = requests.get(link).text
	soup=bs4.BeautifulSoup(res,'html.parser')

	set=soup.find_all('img',limit=1000,recursive=True)

	for each in set:
		if each.get("src")!= None:
			if each.get("src").endswith(".jpg"):
				#doimage(('https://pixabay.com'+each.get("src"))[:-9]+'_960_720.jpg')
				print(('https://pixabay.com'+each.get("src"))[:-9]+'_960_720.jpg')
