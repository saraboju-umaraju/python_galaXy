#!/usr/bin/python3
import re
beg=re.compile(r'^hello')
mo=beg.search('hello')
print(mo.group())
beg=re.compile(r'\d+$') #take out + youll understand
mo=beg.search('hello agent 1212121242')
print(mo.group())
