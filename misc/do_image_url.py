#!/usr/bin/python3
import requests,sys,time
def doimage(link):
        res = requests.get(link)
        res.raise_for_status()
        name=str(time.time())
        image = open(name,'wb')
        for chunk in res.iter_content(100000):
                image.write(chunk)
        image.close()
doimage(sys.argv[1])
