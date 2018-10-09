#!/usr/bin/python3
import pyperclip,threading
print('Password:')
password = input()
pyperclip.copy(password)
threadobj=threading.Thread(taget=su)
threadobj.start()
pyperclip.paste()

