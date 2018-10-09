#!/usr/bin/python3
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
file=open('myCats.py','w')
file.write('cats= ' + pprint.pformat(cats) + '\n')
file.close()
