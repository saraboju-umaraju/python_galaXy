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
res = requests.get('https://www.pexels.com/search/'+key)
soup=bs4.BeautifulSoup(res.content,'html.parser')
list=soup.find_all('img')
for element in list:
	if (((str(element.get('src')).replace('medium','large'))).startswith('http')):
		doimage(((str(element.get('src')).replace('medium','large'))))
