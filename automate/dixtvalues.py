#!/usr/bin/python3
spam = {'color': 'red', 'age': 42}
for index in spam.values():
	print( index )
for index in spam.keys():
	print( index )

for index in spam.items():
	print( index )
print('color' in spam.keys())
