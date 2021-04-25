from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

chrome_driver_path ="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://itmscoaching.herokuapp.com/form")
firstname = driver.find_element_by_id("first-name")
firstname.send_keys("Binh")
time.sleep(1)
lastname = driver.find_element_by_id("last-name")
lastname.send_keys("Nguyen")
time.sleep(1)
jobtitle = driver.find_element_by_id("job-title")
jobtitle.send_keys("Tester")
time.sleep(1)
driver.find_element_by_id("radio-button-3").click()
time.sleep(1)
driver.find_element_by_id("checkbox-2").click()
time.sleep(1)
select = Select(driver.find_element_by_id("select-menu"))
select.select_by_value('3')
time.sleep(1)
day = driver.find_element_by_id("datepicker")
day.send_keys("7/20/2011")
time.sleep(1)
day.send_keys(Keys.ENTER)
driver.close()


