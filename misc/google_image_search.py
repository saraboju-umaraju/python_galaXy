#!/usr/bin/python3
#http://webapps.stackexchange.com/questions/58550/what-does-tbm-mean-in-google-search
import webbrowser,requests,bs4
key='hard'
link="https://www.google.co.in/search?q="+key+"&source=lnms&tbm=isch"
#webbrowser.open(link)
res = requests.get(link).text
print(res)
soup=bs4.BeautifulSoup(res,'html.parser')
#print(soup.prettify())
print(type(soup.find('img')))
for tag in soup.find_all('img'):
	print(tag)
print(soup.find('img').get("src"))
#print(soup.findAll('img'))
print(soup.find('img',{'class':"rg_i"}))
#print(soup.find_all('img',limit=None))
#print(soup.find_all('img'))
