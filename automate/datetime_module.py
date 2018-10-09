#!/usr/bin/python3
import datetime
import time
print(datetime.datetime.now())
dt = datetime.datetime.now()
thousanddays=datetime.datetime.timedelta(days=1000)
dt+thousanddays
print(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
print(datetime.datetime.fromtimestamp(time.time()))
