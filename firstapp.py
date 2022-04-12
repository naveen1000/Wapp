from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
driver = webdriver.Chrome(r"C:\Users\naveen.simma\Desktop\Projects\First_Py_Selenium\chromedriver.exe") 
driver.get("https://www.google.com/")
time.sleep(5) 
print(driver.title) 
print(driver.current_url) 
driver.close()