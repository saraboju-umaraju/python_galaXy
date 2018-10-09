#!/usr/bin/python3
import re
new=re.compile(r'ROBO',re.I)
mo=new.search('robo')
print(mo.group())
