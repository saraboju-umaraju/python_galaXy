#!/usr/bin/python3
import bs4
soup = bs4.BeautifulSoup(open('test.html'))
listed = soup.select('span')[0]
''' /////////
print(str(listed))
'''
print(listed.get('id'))

