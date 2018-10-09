#!/usr/bin/python3
import shutil,os,send2trash
#print(shutil.copytree('testone' , 'testone_backup'))
#print(shutil.copy('one' , 'two'))
#print(shutil.move('one' , 'two'))
#os.unlink('somefile')
#os.rmdir('emptydir')
#shutil.rmtree('dirwithfiles')
#print(os.listdir())
for name in os.listdir():
	if not name.endswith('.py'):
		print(name)

file=open('send2trash.txt' ,'w')
file.write('some data goes here')
file.close()
send2trash.send2trash('send2trash.txt')
