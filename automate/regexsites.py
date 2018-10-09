#!/usr/bin/python3
import re
web=re.compile('w{3}.[a-zA-z.0-9_+-]+.[a-zA-z]')
new=web.search('www.google123.uma')
print(new.group())
