import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome

driver = Chrome()

driver.get('https://www.twitter.com/i/flow/login')

email = input("Enter email: ")
password = input("Enter password: ")
uname = input("Enter username: ")
url = input("give me an url to scan:\n")#https://twitter.com/search?q=%23ClimateActionNow&src=trend_click&f=live&vertical=trends
filename = "output.txt"#change file name to whatever you want
counter = 0

def scraper(card):
    username = card.find_elements_by_xpath('.//span')
    username = username[0].text
    user_id = card.find_elements_by_xpath('.//span[contains(text(),"@")]')
    user_id = user_id[0].text
    try:
        date_time = card.find_elements_by_xpath('.//time')
        date_time = date_time[0].get_attribute('datetime')
        date_time = date_time.replace("T"," ")
        date_time = date_time.replace(".",":")
        date_time = date_time.replace("Z","")
        date_time = datetime.fromisoformat(date_time)
    except:
        date_time = "sponsored tweet"
    tweet_content = card.find_element_by_xpath('.//div/div/div/div[2]/div[2]/div[2]/div[1]/div')
    tweet_content = tweet_content.text
    responding_to = card.find_element_by_xpath('.//div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]').text
    
    with open(filename, 'ab') as f:
        output = 'Tweet Number: ' + str(counter) + '\n' + 'Username: '+ username + '\n' + 'User Handle: ' + user_id + '\n' + 'Content:\n' + tweet_content + '\n\n\n\n'
        f.write(output.encode())

    print(user_id,"             ",date_time)
    
    print('\n')
        
    print(tweet_content)
        
    print('\n')

    print(responding_to)
        
    return user_id


#log in
try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(email)
    time.sleep(2)
except:
    print('Error')

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(Keys.RETURN)
    time.sleep(2)
except:
    print('Error')

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='text']"))).send_keys(uname)
    time.sleep(2)
except:
    print('Error')

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='text']"))).send_keys(Keys.RETURN)
    time.sleep(2)
except:
    print('Error')

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(password)
    time.sleep(2)
except:
    print('Error passss')

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(Keys.RETURN)
    time.sleep(2)
except:
    print('Error pass')

driver.get(url)

#around 1000 tweets per hour
while True:
    cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')# gets tweets
    try:
        for card in cards:
            
            scraper(card)#calls the scraper
            counter+=1
            time.sleep(1)
            
    except Exception as error:
        print(error)
        print('\n')
        print("Twitter is slow wait 4 seconds and it will continue...")
        time.sleep(4)
   
    
    for i in range(9): # adjust integer value for how many times to scroll per cycle
       # edit the speed to your needs
       driver.execute_script("window.scrollBy(0, 250)")
       # you can change time intervels between very scrolling
       time.sleep(1)


