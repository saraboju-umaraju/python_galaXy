#!/usr/bin/python3
import threading,time
def takenap():
	time.sleep(2)
	print('wake up')
threadobj = threading.Thread(target=takenap)
threadobj.start()

print('end')
