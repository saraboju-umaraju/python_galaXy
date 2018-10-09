#!/usr/bin/python3
import csv

with open('some.csv') as csvfile:
	readCSV=csv.reader(csvfile,delimiter=' ')
	colors=[]	
	date=[]
	for row in readCSV:
		#print(row[0])
		colors.append(row[3])
		date.append(row[0])
print(date)
print(colors)
try:
	what=input('color date')
	if what in colors:
		x=colors.index(what)
		print(date[x])
except Exception as e:
	print(e)
