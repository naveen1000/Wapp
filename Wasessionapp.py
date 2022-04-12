from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

def _wait_for_presence_of_an_element(browser, selector): 
    element = None
    try: 
        element = WebDriverWait(browser, 600).until( 
           EC.presence_of_element_located(selector) 
        ) 
    except: 
        pass
    finally: 
        return element 

 def sessionGenerator(sessionFilePath): 
    # 1.1 Open Chrome browser 
    browser = webdriver.Chrome()  
    # 1.2 Open Web Whatsapp 

    browser.get("https://web.whatsapp.com/") 

  

    # 1.3 Ask user to scan QR code 

    print("Waiting for QR code scan...") 

  

    # 1.4 Wait for QR code to be scanned 

    _wait_for_presence_of_an_element( 

      browser, MAIN_SEARCH_BAR__SEARCH_ICON) 

  

    # 1.5 Execute javascript in browser and  

    # extract the session text 

    session = browser.execute_script(EXTRACT_SESSION) 

  

    # 1.6 Save file with session text file with 

    # custom file extension ".wa" 

    with open(sessionFilePath, "w", encoding="utf-8") as sessionFile: 

        sessionFile.write(str(session)) 

  

    print("Your session file is saved to: " + sessionFilePath) 

  

    # 1.7 Close the browser 

    browser.close()       