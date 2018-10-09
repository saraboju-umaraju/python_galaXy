#!/usr/bin/python3
import requests,bs4,os,subprocess
import time
while True:
	resp = requests.get('http://www.espncricinfo.com/india-v-england-2016-17/engine/match/1034811.html')
	soup=bs4.BeautifulSoup(resp.content,"html.parser")
	subprocess.Popen(['notify-send' , '-u', 'critical', str(soup.title.text.split('|')[0])])
	time.sleep(45)

