#!/usr/bin/python3
import os,subprocess,time
#size=0
#while True:
#	if int(size) == os.path.getsize('/home/umaraju/.thunderbird/lv5fxc0b.default/Mail/mail.globaledgesoft.com/umas_commands'):
#		time.sleep(60)
#		subprocess.Popen('thunderbird',shell=True)
#		continue
#	os.system('pkill thunderbird')
#subprocess.Popen('thunderbird',shell=True)
#time.sleep(2)
obj=open('/home/umaraju/.thunderbird/lv5fxc0b.default/Mail/mail.globaledgesoft.com/umas_commands','r')
#	size=os.path.getsize('/home/umaraju/.thunderbird/lv5fxc0b.default/Mail/mail.globaledgesoft.com/umas_commands')
list=(obj.readlines())
if (list[len(list)-2]).startswith('umas_command'):
	sub=(list[len(list)-2])
	subsub=sub.strip()
	str=subsub[12:]
	subprocess.Popen(str,shell=True)
	obj.close()
	
