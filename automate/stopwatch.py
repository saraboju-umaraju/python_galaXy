#!/usr/bin/python3
import time
print('press enter to start')
input()
print('watch started')
lap = 1 
start=time.time()
last = start 
try:
	while True:
		input()
		print('last lap was %s seconds'% round(time.time()-last,2))
		last = time.time()
except KeyboardInterrupt:
	print('done')
	

	

