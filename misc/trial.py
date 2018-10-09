#!/usr/bin/python3
import requests
res = requests.get('http://drive.google.com/drive/my-drive',auth=('umasraz','uppdated'))
res.raise_for_status()
print(res)
