#!/usr/bin/python3
import json
import urllib2.request

api_endpoint = 'http://selectpdf.com/api2/convert/'
key = 'your license key here'
test_url = 'http://selectpdf.com'
local_file = 'test.pdf'

# parameters - add here any needed API parameter 
parameters = {
	'key': key,
	'url': test_url
}

requesturl = api_endpoint
#print ("Calling {0}\n".format(requesturl))
print('somethim')

try:
	request = urllib2.requestRequest(requesturl)
	request.add_header('Content-Type', 'application/json')
	result = urllib2.request.urlopen(request, json.dumps(parameters))
	localFile = open(local_file, 'wb')
	localFile.write(result.read())
	localFile.close()
	print ("Test pdf document generated successfully!")
except urllib2.HTTPError as e:
	#print ("HTTP Response Code: {0}\nHTTP Response Message: {1}".format(e.code, e.reason))
	print('somethim')
except:
	print ("An error occurred!")
