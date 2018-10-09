#!/usr/bin/python3
import copy
list=list('hello')
spam=list
spam2=copy.copy(list)
spam2[1]='changed'
print(spam,spam2)
