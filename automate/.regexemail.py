i#!/usr/bin/python3
import re
email=re.compile(r'[a-zA-z0-9._%+-]+@[a-zA-z0-9._%+-]+\.[a-zA-z0-9._%+-]+' )
mo=email.findall('my name is umaraju and my email is umasraz@gmail.com my secondary mail is usraj222@gmail.com')
print(mo)
phno=re.compile(r'((\+\d\d)?(\d{10}))')
mo=phno.findall('iam umasraz my mobile 9550050426 and secondary is +918686510685')
print(mo)
#print(mo)
