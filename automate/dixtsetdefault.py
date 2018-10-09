#!/usr/bin/python3
spam = {'name': 'Poo', 'age': 5}
spam.setdefault('color','black')
print(spam)
spam.setdefault('color','white')
print(spam)

message='my name is saraboju umaraju chary in whole'
count={}
for char in message :
	count.setdefault(char,0)
	count[char]=count[char]+1
print(count)	
