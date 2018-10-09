#!/usr/bin/python3
def umas(x,y=1,z=1):	
	if x <= 1:	
		raise Exception('x must be gt 1')
	
#tup=((1,1,3),(2,2,2),(3,3,3))
#for x,y,z in tup:
#	umas(x,y,z)
try:
	umas(1)
except:
	print('gotcha')
