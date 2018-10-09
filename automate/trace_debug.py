#!/usr/bin/python3
import traceback
try:	
	raise Exception('this is manual')
except:
	error=open('error_trace.log','w')
	error.write(traceback.format_exc())
	error.close()
