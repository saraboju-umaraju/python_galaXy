#!/usr/bin/python3
def var(*args):
	print(args)
	new=0
	for i in args:
		print(i)
		print(type(i))
	#	new+=i
var(1,2,3,'var')
