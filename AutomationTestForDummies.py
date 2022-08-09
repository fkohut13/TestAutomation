from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
##This is just a Hello World Automation Test that i created

s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s) 
driver.get("https://dummies.com")
driver.maximize_window()
print(driver.title)
search_box = driver.find_element(By.ID,"__BVID__19")
search_box.send_keys("Beginning Programming All-in-One For Dummies")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

driver.execute_script("window.scrollBy(0,600)","")
time.sleep(3)
link = driver.find_element(By.LINK_TEXT,"Beginning Programming All-in-One For Dummies")
link.click()
time.sleep(3)
amazonclassname= driver.find_element(By.XPATH,"//*[@id='app']/div/section/div/div[2]/div/div/div[2]/div[3]/a")
amazonclassname.click()
time.sleep(10)
driver.quit()

##Made by fkohut13





