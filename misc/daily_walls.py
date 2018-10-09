#!/usr/bin/python3
import time,datetime
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
import os,requests,subprocess,datetime


#Variables:
idx = '0' #defines the day of the picture: 0 = today, 1 = yesterday, ... 20.

def doimage(link):
	res = requests.get(link)
	res.raise_for_status()
	today = datetime.datetime.now()
	name= 'Bimages' +'/'+ str(today.strftime('%y_%m_%d'))+'.jpg'
	image = open(name,'wb')
	for chunk in res.iter_content(100000):
		image.write(chunk)
	set(name)
	image.close()

def set(picPath):
	#os.system('gsettings set org.gnome.desktop.background picture-uri file://' + str(os.path.abspath(picPath)))
	subprocess.Popen('gsettings set org.gnome.desktop.background picture-uri file://' + str(os.path.abspath(picPath)),shell=True)
	return

import bs4,requests
re=requests.get('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=ru-RU')
soup=bs4.BeautifulSoup(re.content,'xml')
print(soup.url)
while True:
	usock = urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=' + idx + '&n=1&mkt=ru-RU') #ru-RU, because they always have 1920x1200 resolution pictures
	xmldoc = minidom.parse(usock)
	#print(xmldoc)
	for element in xmldoc.getElementsByTagName('url'):
		url = 'http://www.bing.com' + element.firstChild.nodeValue
	#print(url)
	doimage(url.replace('_1366x768', '_1920x1200'))
	#dt=datetime.timedelta(days=1)
	time.sleep(24*60*60)
