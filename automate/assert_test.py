#!/usr/bin/python3
length='one'
assert length=='one','length must be one'
length='two'
try:
	assert length=='one','length must be one'
except:
	print('assertion exception')
