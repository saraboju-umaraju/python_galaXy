#!/usr/bin/python3
import os,re,shutil
#for name in os.listdir():
	#if name.endswith('.hello'):
		#print(name)
obj=re.compile('[A-Za-z0-9]+.hello')
for name in os.listdir():
	go=obj.search(name)
	if go is not None:
		#print(go.group())
		new=name.split('.')
		shutil.move(name,new[0]+'some_extension')
