#!/usr/bin/python3
listed=['name' ,12, 12.12 ,True,[1,2,3]]
print(listed)
del(listed[1])
length=len(listed)
listed[1]=12
listed=listed+[1,2,3]
print(len(listed))
print(listed[1:3])
#print(listed[4][1])
listed=listed*3
