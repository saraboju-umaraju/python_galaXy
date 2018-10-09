#!/usr/bin/python3
petlist = ['cat' , 'dog' , 'horse' , 'man']
print('enter any pet name')
name=input()
if name in petlist:
	print('i have that species')
else:
	print('i dont have such species')

