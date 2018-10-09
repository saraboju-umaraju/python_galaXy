#!/usr/bin/python3
def fun():
	global eggs
	print(eggs)
	eggs=12
	print(eggs)
eggs=123
fun()
print(eggs)
