#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import sys,time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

#driver.get("https://172.16.2.9")
driver.get("https://spandana.globaledgesoft.com/")
search_fieldu = driver.find_element_by_id("username")
search_fieldp = driver.find_element_by_id("password")
search_fieldu.clear()
search_fieldp.clear()
search_fieldu.send_keys("u.saraboju")
search_fieldp.send_keys("#")
search_fieldu.submit()
#driver.switch_to_window(driver.window_handles[0])

lists= driver.find_elements_by_class_name("downarrowclass")

qms=lists[3]
driver.get("https://spandana.globaledgesoft.com/QMS/TimeSheet/TimesheetIndex.aspx")
#qms.click()
#tsheet=driver.find_elements_by_link_text("Timesheet")
#tsheet[0].click()
#file_appr=driver.find_elements_by_link_text("File/View/Approve Timesheet")
#file_appr[0].click()
#if len(driver.window_handles) == 2:
#driver.close()
#driver.switch_to.window(window_name=driver.window_handles[-1])
#content = driver.find_element_by_css_selector('input.Activity')
#print(content)
print("hello world")
print(driver.find_element_by_xpath("//select[@id='remarkContentHiddenTextarea']"))
select = Select(driver.find_element_by_xpath("""//input[@name='DHrs_ClientState']"""))
select.select_by_index(2)
print("hello world")
elem = driver.find_element_by_name(objectVal)
for option in elem.find_elements_by_tag_name('option'):
	if option.text == value:
		break
	else:
		ARROW_DOWN = u'\ue015'
		elem.send_keys(ARROW_DOWN)

#hour=driver.find_elements_by_class_name("rcbReadOnly")
print(hour)
#time.sleep(3)
#view_sheet[0].click()
#print(view_sheet[0])
content = driver.find_element_by_css_selector('input.ddlEPhase_Input')
print(content)
#hour[0] = "8"
'''i=0
for listitem in tsheet:
   listitem.click()
   time.sleep(4)
   i=i+1
   if(i>10):
      break
'''
time.sleep(1000)
#view_sheet[0].click()
driver.quit()
