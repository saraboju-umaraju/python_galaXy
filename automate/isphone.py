#!/usr/bin/python3
def isphno(item):
	if len(item) != 10 :
		return False
	for i in range(0,10):
		if not item[i].isdecimal():
			return False
	return True
print(isphno('9550050426'))
print(isphno('umasraz'))
text='my name is umaraju and my no is 7204443644 9550050426'
for i in range(len(text)):
	if isphno(text[i:i+12]):
		print(text[i:i+12])
print('done')
