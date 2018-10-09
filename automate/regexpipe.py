#!/usr/bin/python3
import re
match=re.compile(r'ubatman|iron man')
mo=match.search('i love batman and iron man')
print(mo.group())
bat=re.compile(r'bat(man|hat|mobile|laptop)')
mo=bat.search('i have a batlaptop')
print(mo.group())


new=re.compile('bat(wo)?man')
mo3=new.search('i love to meet batman')
print(mo3.group())
mo4=new.search('i love to meet batwoman')
print(mo4.group())

phno=re.compile(r'(\+\d\d)?\d\d\d\d\d\d\d\d\d\d')
mo=phno.search('+919550050426')
print(mo.group())
mo=phno.search('9550050526')
print(mo.group())

new=re.compile(r'bat(wo)*man')
mo=new.search('advent or batwowowowowowowoman')
print(mo.group())

new=re.compile(r'bat(wo)+man')
mo=new.search('advent or batwowowowowowowoman')
print(mo.group())
mo=new.search('advent or batman')
if mo==None:
	print("no such")
else:
	print(mo.group())

new=re.compile(r'(ha){3,5}')
mo=new.search('hahahaha')
print(mo.group())
new=re.compile('(\d\d\d)-(\d\d\d\d)')
print(new.findall('123-4567 234-6789'))
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
