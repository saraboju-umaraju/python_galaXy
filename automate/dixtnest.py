#!/usr/bin/python3
def tot(item):
	global dict
	num=0 
	for i, j in dict.items():
		num = num+j.get(item ,0)
	return num

dict={'uma':{'apples':12 , 'nuts':12} , 'kan':{'nuts':12 , 'apples':10} , 'kar': {'bats':0 , 'pads':12} }
print(tot('apples'))
print(tot('nuts'))
print(tot('bats'))
print(tot('pads'))
		
