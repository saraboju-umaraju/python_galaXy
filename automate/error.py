#!/usr/bin/python3
def spam(denom):
	try:
		return 42/denom
	except:
		print('Invalid argument')
#print(spam(1))
print(spam(0))
	
