#!/usr/bin/python3
import re
vowel=re.compile(r'[aeiouAEIOU]')
vowel=re.compile(r'[a-zA-z)-9]')
print(vowel.findall('Robocop eats baby food. BABY FOOD.'))

vowel=re.compile(r'[^aeiouAEIOU]')
print(vowel.findall('Robocop eats baby food. BABY FOOD.'))
at=re.compile(r'.at')
print(at.findall('The cat in the hat sat on the flat mat.'))
name = re.compile(r'First Name: (.*) Last Name: (.*)')
mo=name.search('First Name: uma Last Name: raju')
print(mo.group(1))
print(mo.group(2))
