#!/usr/bin/python3
import time
def res():
	product = 1
	for i in range(1,100000):
		product*=i
	return product
start = time.time()
#re = res()
#print('result is %s digits long ' % len(str(re)))
#print('calculation took %s seconds' % str( time.time() - start))
time.sleep(2)
print(round(start,2))
print(round(start))
