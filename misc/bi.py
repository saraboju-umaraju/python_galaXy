#!/usr/bin/python3
import requests,bs4,sys,time
def doimage(link):
        res = requests.get(link)
        res.raise_for_status()
        name=str(time.time())
        image = open(name,'wb')
        for chunk in res.iter_content(100000):
                image.write(chunk)
        image.close()

if len(sys.argv ) < 2:
        key='art'
else:
        key=sys.argv[1]
res = requests.get('http://www.bing.com/images/search?q='+key)
soup=bs4.BeautifulSoup(res.content,'xml')
list=soup.find_all('img')
for element in list:
	if str(element.get('src')).startswith('http'):
		doimage(str(element.get('src')))
