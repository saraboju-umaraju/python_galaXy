#!/usr/bin/python3
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# a little validation part ###res.raise_for_status()
print(type(res))
if res.status_code == requests.codes.ok :
	print(len(res.text))
	print(res)
