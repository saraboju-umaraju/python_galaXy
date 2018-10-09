#!/usr/bin/python3
import os
os.chdir('/usr/src')
list=[]
for file in os.listdir():
	if file.startswith('linux-'):
		list.append(file)
listvers=[]
for each in list:
	 listvers.append(each.split('-'))
vers=[]
for each in listvers:
	vers.append(each[1])
sv=[]
for each in vers:
	sv.append(each.split('.'))
sv.sort()
output='.'.join(sv[len(sv)-1])
output= [ 'linux' ,output]
output='-'.join(output)
print(output)
