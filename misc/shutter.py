#!/usr/bin/python3
#http://webapps.stackexchange.com/questions/58550/what-does-tbm-mean-in-google-search
import webbrowser,requests,bs4
import time,re
import requests
import sys,time
def find_max(link):
	print(link)
	res = requests.get(link)
	res.raise_for_status()
	res = requests.get(link).text
	soup=bs4.BeautifulSoup(res,'html.parser')
	set=soup.find_all('span',{"class":"page-max"})
	res=re.compile(r"\d\d,\d\d\d|\d,\d\d\d|\d,\d\d|(\d\d)|\d")
	mo=res.search(str(set))
	print((str(mo.group())).replace(',',''))
	return (str(mo.group())).replace(',','')

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
link='https://www.shutterstock.com/search?&searchterm='+key
for num in range( 1, int(find_max(link))):
	link='https://www.shutterstock.com/search?&searchterm='+key+'&page='+ str(num)
	res = requests.get(link)
	res.raise_for_status()
	res = requests.get(link).text
	soup=bs4.BeautifulSoup(res,'html.parser')

	set=soup.find_all('img',limit=1000,recursive=True)

	for each in set:
		if each.get("src")!= None:
			if each.get("src").endswith(".jpg"):
				#doimage(('https://pixabay.com'+each.get("src"))[:-9]+'_960_720.jpg')
				doimage('https:'+each.get("src"))
				print('https:'+each.get("src"))
