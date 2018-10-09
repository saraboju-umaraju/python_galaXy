#!/usr/bin/python3
#http://webapps.stackexchange.com/questions/58550/what-does-tbm-mean-in-google-search
import webbrowser,requests,bs4
import time
import requests
import sys,time
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
#link="https://www.google.co.in/search?q="+key+"&source=lnms&tbm=isch"
#webbrowser.open(link)
#link='https://pixabay.com/'
link='https://pixabay.com/en/photos/?cat='+key
print(link)
res = requests.get(link)
res.raise_for_status()
res = requests.get(link).text
soup=bs4.BeautifulSoup(res,'html.parser')




set=soup.find_all('img',limit=1000,recursive=True)
#print(set)
#sys.exit()
for each in set:
	if each.get("src")!= None:
		if each.get("src").endswith(".jpg"):
			#doimage(('https://pixabay.com'+each.get("src")).replace('__340','_960_720'))
			print(('https://pixabay.com'+each.get("src"))[:-9]+'_960_720.jpg')



#print(soup.find('img',{'class':"rg_i"}))
#print(soup.find_all('img',limit=None))
#print(soup.find_all('img'))
