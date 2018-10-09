#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,time
# create a new Firefox session
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
 
# navigate to the application home page
driver.get("https://mail.globaledgesoft.com")
# get the search textbox
search_fieldu = driver.find_element_by_id("username")
print(search_fieldu)
if search_fieldu != None:
	search_fieldp = driver.find_element_by_id("password")
	search_fieldu.clear()
	search_fieldp.clear()
	#enter search keyword and submit
	search_fieldu.send_keys("u.saraboju")
	search_fieldp.send_keys("Global@11")
	search_fieldu.submit()
	search_fieldp.submit()

sys.exit(1) 
alert = driver.switch_to.alert();
alert.accept();
# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
#lists= driver.find_elements_by_class_name("downarrowclass")
 
# get the number of elements found
#print ("Found " + str(len(lists)) + "searches:")
 
# iterate through each element and print the text that is
# name of the search
'''i=0
for listitem in lists:
   listitem.click()
   time.sleep(5)
   i=i+1
   if(i>10):
      break
'''
#qms=lists[3]
#qms.click()
# close the browser window
time.sleep(5)
driver.quit()
