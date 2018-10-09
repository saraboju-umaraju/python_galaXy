#!/usr/bin/python3
import random
class student():
	def __init__(self,name='unknown'):
		print('instance just been created ' + name)
		self.name=name
	def cur_act(self):
		print('this is cur_method')
	def __del__(self):
		print('destroyed')

uma=student("uma")
raj=student()
uma.cur_act()
raj.cur_act()
