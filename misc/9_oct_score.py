#!/usr/bin/python3
import bs4,requests,time,subprocess
while True:
	link=requests.get('http://www.news18.com/cricketnext/live-score/full/england-in-india-5-test-series-2016/india-vs-england/inen11092016181704.html')
	link.raise_for_status()
	soup=bs4.BeautifulSoup(link.content,'html.parser')
	#score=soup.find('span',attrs={'class':'team-runs '})
	#team=soup.find('span',attrs={'id':'team_name_1'})
	#overs=soup.find('span',attrs={'id':'team_overs_1'})
	#print(soup.prettify())
	score=soup.find('title',attrs={'id':'score_in_title'})	
	print(soup.find_all('title'))
	#print(score.text[:85])
	#print(overs.text)
	#print(score.text)
	#subprocess.Popen(['notify-send' , '-u', 'critical', score.text.split('|')[0]])
	time.sleep(60)
