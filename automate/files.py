#!/usr/bin/python3
import os
myfiles = ['1.py','2.py','3.py','4.py']
for index in  myfiles:
	print(os.path.join('.',index))
print(os.getcwd())
#os.chdir('/')
#os.makedirs('./12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/uma.py')
#os.removedirs('./12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/12/uma.py')
print(os.path.abspath('.'))
print(os.path.abspath('__pycache__'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print(os.path.dirname(os.path.abspath('.')))
print(os.path.basename(os.path.abspath('.')))
print(os.path.relpath('.' , '../..'))
tuple=os.path.split(os.path.abspath('.'))
print(tuple)
print((os.getcwd()).split(os.path.sep))
print(os.path.getsize('./files.py'))
#print(os.listdir())
list=os.listdir()
tot=0
for each in list:
	tot+=os.path.getsize(each)
print(tot)
print(os.path.exists('./files.py'))
print(os.path.isfile('./files.py'))
print(os.path.isdir('./files.py'))
