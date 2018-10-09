#!/usr/bin/python3
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
newf = open('romeojuliet.txt' ,'wb')
for data in res.iter_content(100000):
	newf.write(data)

newf.close()
