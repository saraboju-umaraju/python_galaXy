#!/usr/bin/python3
#http://webapps.stackexchange.com/questions/58550/what-does-tbm-mean-in-google-search
import webbrowser,requests,bs4
import time
import requests
import sys,time
def doimage(link):
        res = requests.get(link)
#res = requests.get('http://www.sideshowtoy.com/wp-content/uploads/2016/02/dc-comics-the-joker-the-dark-knight-premium-format-feature-300251-1.jpg')
        res.raise_for_status()
        name=str(time.time())
        image = open(name,'wb')
        for chunk in res.iter_content(100000):
                image.write(chunk)
        image.close()
if len(sys.argv ) < 2:
	key='love'
else: 
	key=sys.argv[1]
link="https://www.google.co.in/search?q="+key+"&source=lnms&tbm=isch"
#webbrowser.open(link)
#link='http://picsphotosimages.blogspot.in/'
res = requests.get(link)
res.raise_for_status()
res = requests.get(link).text
soup=bs4.BeautifulSoup(res,'html.parser')
#print(soup.prettify())
#print(type(soup.find('img')))
for tag in soup.find_all('img'):
	print(tag)
#print(soup.find('img').get("src"))
#set=soup.find_all('img',{'alt':'Image result for hard'})
#set=soup.find_all('a')
#for each in set:
#	link=each.get("src")
#	doimage(link)
#set=soup.find_all('div', attrs={'class':"rg_di rg_bx rg_el ivg-i "})
#print(set)

sys.exit(1)
set=soup.find_all('a')
for each in set:
	if each.get("href")!= None:
		if each.get("href").endswith(".jpg"):
			doimage(each.get("href"))



#print(soup.find('img',{'class':"rg_i"}))
#print(soup.find_all('img',limit=None))
#print(soup.find_all('img'))
