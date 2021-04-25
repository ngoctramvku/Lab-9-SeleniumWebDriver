from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path ="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
get_title=driver.title
print(get_title)
time.sleep(3)
driver.close()