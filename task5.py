from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path ="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
driver.set_window_size(1920,1080)
curent_url= driver.current_url
print(curent_url)
time.sleep(3)
driver.close()