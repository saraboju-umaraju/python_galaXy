#!/usr/bin/python3
import bs4,requests,tarfile
import os,shutil,subprocess,sys,getpass

if getpass.getuser() != "root":
	subprocess.call(['notify-send','-u','critical', 'execute with su permissions' ])
	sys.exit()
res = requests.get('https://www.kernel.org/').text
obj = bs4.BeautifulSoup(res,"html.parser")

validate=obj.find('td',attrs={'id':'latest_link'}).text
temp_file=open('/tmp/temp_file.txt','w')
subprocess.call(['uname','-r'],stdout=temp_file)

with open("/tmp/temp_file.txt" , 'r') as filed:
	output=filed.read()

if validate.strip('\n') in str(os.listdir('/usr/src')):
	subprocess.call(['notify-send','-u','critical', 'you already have downloaded this kernel' ])
	sys.exit()
if output in validate:
	subprocess.call(['notify-send','-u','critical', 'you already are running on latest kernel' ])
	sys.exit()
else:
	subprocess.call(['notify-send','-u','critical', 'downloading_latest_kernel'+' '+validate.strip("\n") ])

new=obj.find('td' , attrs={'id':'latest_link'})
allnew=new.a
new=requests.get(allnew.get("href"))
try:
	new.raise_for_status()
except:
	subprocess.call(['notify-send','-u','critical',"some problem with kernel server"])
	sys.exit()

fil=open('/tmp/latest_linux' , 'wb')
for chunk in new.iter_content(100000):
	fil.write(chunk)
fil.close()
with tarfile.open('/tmp/latest_linux') as f:
	uma=f.extractall('/usr/src/')	
os.chdir('/usr/src')
listed=[]
for file in os.listdir():
	if os.path.isdir(file):
		if 'vmlinux' not in os.listdir(file):
			shutil.copy('/opt/make_script.sh',file)
			break;
os.chdir(os.path.join('/usr/src' ,file))
subprocess.call(['chmod','+x','make_script.sh'])
if subprocess.call(['./make_script.sh']):
	subprocess.call(['notify-send','-u','critical', '"kernel installed...!"' ])
