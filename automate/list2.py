#!/usr/bin/python3
catnames = [] 
while 1:
	print('enter cat name or nothing')
	name=input()
	if name == '':
		break 
	catnames=catnames+[name]
print('cats are')
for sename in catnames: #for index in range(len(catnames))
	print('  ' +sename)
print(catnames)
print( 1 in catnames)
