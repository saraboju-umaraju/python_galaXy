#!/usr/bin/python3
import bs4,requests
import bs4
data = []

new_file = open('1.html')
soup=bs4.BeautifulSoup(new_file.read(),"html.parser")
table = soup.find('table')#, attrs={'class':'lineItemsTable'})

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print(cols)
    print("\n")
    data.append([ele for ele in cols if ele]) # Get rid of empty values
#print(data)
