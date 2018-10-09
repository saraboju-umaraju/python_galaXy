#!/usr/bin/python3
import re
phno=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phno.search('my number is 123-343-1232')
print(mo.groups())
print(mo.group())
areacode,mainnumber=mo.groups()
print(areacode)
phno=re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo=phno.search('my number is (123)-343-1232')
print(mo.group())
