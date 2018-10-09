#!/usr/bin/python3
import datetime,time
today = datetime.datetime.now()
print(today.strftime('%y_%m_%d %H %M %S'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
