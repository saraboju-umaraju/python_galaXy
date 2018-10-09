#!/usr/bin/python3
import pprint
message='my name is saraboju umaraju chary in whole'
count={}
for char in message :
	count.setdefault(char,0)
	count[char]=count[char]+1
pprint.pprint(count)	
print(pprint.pformat(count))
