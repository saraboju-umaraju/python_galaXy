#!/usr/bin/python3
import requests,bs4,re
link='https://pixabay.com/en/photos/?image_type=&q=america'
res=requests.get(link).text
soup=bs4.BeautifulSoup(res,'html.parser')
limit=soup.find('input',{'name':'pagi'}).text
limit=limit.strip()
#new=re.compile("\d+|\d{4}+|\d{3}+|\d{2}+|\d{1}+")
new=re.compile("\d{1,5}")
mo=new.search(limit)
print(mo)
print(mo.group())
