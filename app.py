from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# XPath selectors
NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/header[1]/div[2]/div[1]/span[1]/div[2]/div[1]/span[1]'
INPUT_TXT_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
ONLINE_STATUS_LABEL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'

# Replace below with the list of targets to be tracked
TARGETS = {'"contactName1"': '7287075568'}

#CHROME_DATA_PATH = "user-data-dir=C:\\Users\\naveen.simma\\Desktop\\Projects\\First_Py_Selenium"
#CHROME_DATA_PATH = "user-data-dir=/app"
optionss = webdriver.ChromeOptions()
#Start Added for Heroku
#optionss.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#optionss.add_argument("--headless")
#optionss.add_argument("--no-sandbox")
#optionss.add_argument("--disable-dev-sh-usage")
#End for Heroku

# Change user-data-dir path with your local path, where you want to save session
#optionss.add_argument(CHROME_DATA_PATH)
# Replace below path with the absolute path
browser = webdriver.Chrome(r'C:\Users\naveen.simma\Desktop\Projects\First_Py_Selenium\chromedriver.exe',options=optionss)
#browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=optionss)
# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

while True:
    # Clear screen
    #os.system('cls')
    #print('cls')
    # For each target
    for target in TARGETS:
        tryAgain = True

        # Wait untill new chat button is visible
        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

        while (tryAgain):
            try:
                # Click on new chat button
                new_chat_title.click()

                # Wait untill input text box is visible
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))

                time.sleep(0.5)

                # Write phone number
                input_box.send_keys(TARGETS[target])

                time.sleep(1)

                # Press enter to confirm the phone number
                input_box.send_keys(Keys.ENTER)

                time.sleep(5)
                tryAgain = False

                try:
                    try:
                        browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
                        print(target + ' is online')
                        print(browser.find_element_by_xpath(ONLINE_STATUS_LABEL).text)
                    except:
                        print(target + ' is offline')
                    time.sleep(1)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)