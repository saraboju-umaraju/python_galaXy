#!/usr/bin/python3
import shelve
shelf=shelve.open('mydata')
cats=['madabba','meedabba','valladabba']
shelf['cats']=cats
shelf.close()

#another module.py
shf=shelve.open('mydata')
shf['cats']
shf.close()
