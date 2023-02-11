# Importing the neccesary libraries
from lib2to3.pgen2 import driver
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

## This automated test navigates to dummies.com and searches for a book, and then checks its respective amazom page.
s = Service("C:\Program Files (x86)\chromedriver.exe") # Setting up the Chrome driver service
driver = webdriver.Chrome(service=s) # Launching the Chrome browser

driver.get("https://dummies.com") # Navigating to dummies.com
driver.maximize_window() # Maximizing the browser window
search_box = driver.find_element(By.ID,"__BVID__19") # Finding the search box element using its ID 
letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z") # List of letters to be used for the search
random_letter = random.choice(letters) #Chooses a random letter from the list
time.sleep(2)
search_box.send_keys(random_letter) # Entering the random letter in the search box
time.sleep(2)
search_box.send_keys(Keys.RETURN) # Submitting the search query by pressing the return key
time.sleep(2)
Cookies = driver.find_element(By.XPATH,"//button[normalize-space()='Accept']").click() # Finding the 'Accept' button for cookies and clicking it
time.sleep(4)
Results = driver.find_elements(By.PARTIAL_LINK_TEXT,"View Article") # Finding the elements with partial link text "View Article"
time.sleep(2)
selected_results = random.choice(Results) # Choosing a random result

# Performing an action chain on the selected result
actions = ActionChains(driver)
actions.move_to_element(selected_results) 
time.sleep(5)
wait = WebDriverWait(driver, 12) # Setting up a WebDriverWait object
clickable_article = wait.until(EC.element_to_be_clickable(selected_results)) # Using the expected wait for the 
driver.execute_script("arguments[0].click();", selected_results) # Clicking on the selected result using JavaScript
time.sleep(10)
amazonclassname= driver.find_element(By.XPATH,"//a[normalize-space()='Buy On Amazon']") #Finds the buy on amazon element by xpath
clickable_amazon = wait.until(EC.element_to_be_clickable(amazonclassname))
driver.execute_script("arguments[0].click();", amazonclassname) # Clicking on the selected result using JavaScript
amznlink = amazonclassname.get_attribute("href") # Fetches the amazon link
time.sleep(5)
driver.get(amznlink)
book = driver.find_element(By.ID,"productTitle") # Finds the element containing the book's name
book = book.text
driver.quit()
print("The random selected book was:", book)

