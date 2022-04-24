from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import requests

def notify(msg):
    #TelegramChannel chatId -1001181667975   
    #MyChatId 582942300
    url='https://api.telegram.org/bot1193312817:AAGTRlOs3YZHFeDSO_33YTwwewrEaMbLizE/sendMessage?chat_id=582942300&parse_mode=Markdown&text='+msg
    requests.get(url)
    print("notified")

# XPath selectors
NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/header[1]/div[2]/div[1]/span[1]/div[2]/div[1]/span[1]'
INPUT_TXT_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
ONLINE_STATUS_LABEL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'

# Replace below with the list of targets to be tracked
TARGETS = {'"contactName1"': '728707556'}

CHROME_DATA_PATH = "user-data-dir=C:\\Users\\Administrator\\Desktop\\Wapp\\session"
ser = Service("C:\\Users\\Administrator\\Desktop\\Wapp\\chromedriver.exe")
#CHROME_DATA_PATH = "user-data-dir=/app"
options = webdriver.ChromeOptions()
#Start Added for Heroku
#optionss.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#optionss.add_argument("--headless")
#optionss.add_argument("--no-sandbox")
#optionss.add_argument("--disable-dev-sh-usage")
#End for Heroku

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
# Change user-data-dir path with your local path, where you want to save session
options.add_argument(CHROME_DATA_PATH)
# Replace below path with the absolute path
browser = webdriver.Chrome(service=ser,options=options)
#browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=optionss)
# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)
contact1_old_status= 'test1'
contact1_new_status = 'test11'
print('Started..')
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
                        contact1_new_status = browser.find_element(by = By.XPATH ,value= ONLINE_STATUS_LABEL).text
                        #print(target + ' is online')
                        print(contact1_new_status)
                        if contact1_new_status != contact1_old_status:
                            print(contact1_new_status)
                            print(contact1_new_status[19:25])
                            notify(contact1_new_status)
                        contact1_old_status = contact1_new_status
                    except:
                        print('In exception')
                        time.sleep(1)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)
