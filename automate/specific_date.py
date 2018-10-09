#!/usr/bin/python3
import datetime,time
target = datetime.datetime(2016,10,13,10,13,40)
while datetime.datetime.now() < target:
	time.sleep(1)
print("all set to go")
