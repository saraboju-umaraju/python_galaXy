#!/usr/bin/python3
import requests
from lxml import html 
import time
import subprocess
#https://impythonist.wordpress.com/2014/09/07/how-i-satisfied-a-request-from-my-friend-with-python/
while True:
	page=requests.get('http://sports.ndtv.com/cricket/live-scores')
	tree=html.fromstring(page.text)
	score=(tree.xpath('//div[@class="ckt-scr"]/text()')[0].lstrip()).rstrip()
	print(score)
	subprocess.Popen(['notify-send' , '-u', 'critical', score])
	time.sleep(5)
