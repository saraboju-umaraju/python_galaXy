#!/usr/bin/python3
bday = {'uma': '11-may' , 'kan': '18-mar' , 'kar' : 'forgot'}
while 1 :
	print('enter name to know their birthday')
	name=input()
	if name =='':
		break;
	if name in bday:
		print( name + ' bday is ' + bday[name])
	else:
		print('sorry i dont have details for '+name + ' what is theire bday')
		bdaynew=input()
		bday[name]=bdaynew
		print('data base updated')
