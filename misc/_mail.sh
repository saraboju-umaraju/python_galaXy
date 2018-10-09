#! /bin/bash
counter=10
str=`stat /home/umaraju/.thunderbird/lv5fxc0b.default/Mail/mail.globaledgesoft.com/umas_commands | sed '6q;d'|awk {'print $3'}`
./mail_script.py&
while [ $counter -gt 0 ]; do
	#./mail_script.py& 1>/dev/null 2>/dev/null
	sleep 10
	new=`stat /home/umaraju/.thunderbird/lv5fxc0b.default/Mail/mail.globaledgesoft.com/umas_commands | sed '6q;d'|awk {'print $3'}`
	if [ "$new" = "$str" ];then
		echo continuing...
		continue
	else 
		./mail_script.py&
		echo executing
		new=`stat /home/umaraju/.thunderbird/lv5fxc0b.default/Mail/mail.globaledgesoft.com/umas_commands | sed '6q;d'|awk {'print $3'}`
		
	fi
done
