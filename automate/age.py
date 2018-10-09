#!/usr/bin/python3
#if not age.isdecimal() :
while True:
	print("enter your age")
	age=input()
	if age.isdecimal():
		break
	print("enter a number to age")
while True:
	print("select a new password ( numbers and characters are allowed")
	
	passwd=input()

	if passwd.isalnum():
		print("good passwd")
		break 
	else:
		print("bad passwd")
