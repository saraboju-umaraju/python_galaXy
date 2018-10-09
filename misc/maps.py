#!/usr/bin/python3
import webbrowser,sys,pyperclip
if len(sys.argv) > 1 :
	address=''.join(sys.argv[1:])
else:
	address=pyperclip.paste()
webbrowser.open('https://www.google.co.in/maps/place/' + address)
#webbrowser.open('https://spandana.globaledgesoft.com/QMS/TimeSheet/TimesheetIndex.aspx')
