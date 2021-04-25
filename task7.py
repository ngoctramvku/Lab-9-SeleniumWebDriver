from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path ="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
click = driver.find_element_by_link_text("My Account").click()
email= driver.find_element_by_id("reg_email")
email.send_keys("lntram.18it2@vku.udn.vn")
password = driver.find_element_by_id("reg_password")
password.send_keys("ngoctramit2")
password.send_keys(Keys.ENTER)
time.sleep(3)
driver.close()