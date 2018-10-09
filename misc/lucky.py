#!/usr/bin/python3
import sys,bs4,requests,webbrowser
print('Searching Google...!')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
#print(res.text)
soup = bs4.BeautifulSoup(res.text)
links = soup.select('.r a')
#for i in range(len(links)):
#	print(links[i])
for i in range(min(5,len(links))):
	#print((links[i].get('href')))
	#webbrowser.open(str(links[i]))
	webbrowser.open('http://google.com' + links[i].get('href'))
