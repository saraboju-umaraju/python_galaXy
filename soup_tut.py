#!/usr/bin/python3
from bs4 import BeautifulSoup
new_file = open('html_doc.html')
soup = BeautifulSoup(new_file.read() , 'html.parser')
print(soup.prettify())
