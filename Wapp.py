from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time
import os
import requests
import pytz
import mysql.connector

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
TARGETS = {'contactName1': '7287075568'}

UTC = pytz.utc
timeZ_Kl = pytz.timezone('Asia/Kolkata') 

mydb = mysql.connector.connect(
  host="database-1.cyxb0drmxfft.us-east-1.rds.amazonaws.com",
  user="admin",
  password="admin123",
  database="Wadb"
)
mycursor = mydb.cursor()

#CHROME_DATA_PATH = "user-data-dir=C:\\Users\\Administrator\\Desktop\\Wapp\\session"
#ser = Service("C:\\Users\\Administrator\\Desktop\\Wapp\\chromedriver.exe")

CHROME_DATA_PATH = "user-data-dir=C:\\Users\\naveen.simma\\Desktop\\Projects\\Remote\\Wapp\\session"
ser = Service("C:\\Users\\naveen.simma\\Desktop\\Projects\\Remote\\Wapp\\chromedriver.exe")


options = webdriver.ChromeOptions()
#Start Added for Heroku
#optionss.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#optionss.add_argument("--headless")
#optionss.add_argument("--no-sandbox")
#optionss.add_argument("--disable-dev-sh-usage")
#End for Heroku
'''
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
'''
# Change user-data-dir path with your local path, where you want to save session
options.add_argument(CHROME_DATA_PATH)
# Replace below path with the absolute path
browser = webdriver.Chrome(service=ser,options=options)
#browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=optionss)
# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)
contact1_old_status= { "status" : "test1", time: ""}
contact1_new_status = { "status" :"test11", time: ""}

try:
    notify('Started..')
except:
    print('In notify start')


# Wait untill new chat button is visible
 
while True:
    # Clear screen
    #os.system('cls')
    #print('cls')
    try:
        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

        # Click on new chat button
        new_chat_title.click()

        # Wait untill input text box is visible
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))

        time.sleep(0.5)

        # Write phone number
        input_box.send_keys(TARGETS['contactName1'])

        time.sleep(1)

        # Press enter to confirm the phone number
        input_box.send_keys(Keys.ENTER) 

        contact1_new_status['status'] = browser.find_element(by = By.XPATH ,value= ONLINE_STATUS_LABEL).text
        now = datetime.now(timeZ_Kl)
        t = now.strftime("%H:%M")
        #print(target + ' is online')
        #print(contact1_new_status['status'])
        if contact1_new_status['status'] != contact1_old_status['status']:
            if contact1_new_status['status'] == 'online':                                
                print(contact1_new_status['status'] + ' ' + t )
                sql = "insert into Wadb.Wastatus (Contact,Status,Creation_date) VALUES ('7287075568','online',NOW())"
                mycursor.execute(sql)
                mydb.commit()
                #print(contact1_new_status['status'][19:23])
                notify(contact1_new_status['status'] + ' ' + t)
            else:
                print( 'offline' + ' ' + t +  ' ' + contact1_new_status['status'] )
                #print(contact1_new_status['status'][19:23])
                sql = "insert into Wadb.Wastatus (Contact,Status,Creation_date) VALUES ('7287075568','offline',NOW())"
                mycursor.execute(sql)
                mydb.commit()
                try:
                    notify('offline' + ' ' + t + ' ' + contact1_new_status['status'])
                except:
                    print('In Notify')
        contact1_old_status['status'] = contact1_new_status['status']
        time.sleep(7)
    except:
        print('In Exception')    
        time.sleep(9)



