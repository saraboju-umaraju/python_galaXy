#!/usr/bin/python3
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
