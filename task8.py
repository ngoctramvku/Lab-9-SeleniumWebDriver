from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path ="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://the-internet.herokuapp.com/")
click = driver.find_element_by_link_text("Form Authentication").click()
username= driver.find_element_by_id("username")
username.send_keys("tomsmith")
password = driver.find_element_by_id("password")
password.send_keys("SuperSecretPassword!")
password.send_keys(Keys.ENTER)
print(driver.title)
time.sleep(3)
driver.close()