#!/usr/bin/python3
import bs4,requests,time,subprocess
while True:
	link=requests.get('http://www.news18.com/cricketnext/live-score/new-zealand-in-india-5-odi-series-2016/india-vs-new-zealand/innz10262016181606.html').text
	#link.raise_for_code()
	soup=bs4.BeautifulSoup(link,'html.parser')
	#score=soup.find('span',attrs={'class':'team-runs '})
	#team=soup.find('span',attrs={'id':'team_name_1'})
	#overs=soup.find('span',attrs={'id':'team_overs_1'})
	#print(soup.prettify())
	score=soup.find('title',attrs={'id':'score_in_title'})	
	#print(score.text[:85])
	#print(overs.text)
	#print(score.text)
	subprocess.Popen(['notify-send' , '-u', 'critical', score.text.split('|')[0]])
	time.sleep(60)
