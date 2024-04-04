# import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from linkedin_scraper import Person, actions
# from selenium import webdriver

# os.environ['CHROMEDRIVER'] = '/Users/alikbangash/Downloads/chrome-mac-x64'

# driver = webdriver.Chrome()

# email = "aaybangash@gmail.com"
# password = "Mercedes@4557287"
# actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal

# # Add an explicit wait here
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.ID, 'some-id')))

# person = Person("https://www.linkedin.com/in/ali-sarosh-bangash-0413541b9/", driver=driver)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd

PATH = "/Users/alikbangash/Downloads/chromedriver-mac-x64/chromedriver"
USERNAME = "aaybangash@gmail.com"
PASSWORD = "Mercedes@4557287"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service(PATH)

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

driver.get("https://www.linkedin.com/uas/login")

# Wait for the username field to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

email = driver.find_element(By.ID, "username")
email.send_keys(USERNAME)

# Wait for the password field to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

password.send_keys(Keys.RETURN)

post_links = []
post_texts = []
post_names = []

def Scrape_func(a,b,c):
    name = a[28:-1]
    page = a
    time.sleep(10)

    driver.get(page + 'detail/recent-activity/shares/')  
    start=time.time()
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        end=time.time()
        if round(end-start)>25:
            break

    company_page = driver.page_source   

    linkedin_soup = bs(company_page.encode("utf-8"), "lxml")
    linkedin_soup.prettify()
    containers = linkedin_soup.findAll("div",{"class":"occludable-update ember-view"})
    print("Fetching data from account: "+ name)
    iterations = 0
    nos = int(input("Enter number of posts: "))
    for container in containers:

        try:
            text_box = container.find("div",{"class":"feed-shared-update-v2__description-wrapper ember-view"})
            text = text_box.find("span",{"dir":"ltr"})
            b.append(text.text.strip())
            c.append(name)
            iterations += 1
            print(iterations)
            
            if(iterations==nos):
                break

        except:
            pass 

n = int(input("Enter the number of entries: "))
for i in range(n):
    post_links.append(input("Enter the link: "))
for j in range(n):
    Scrape_func(post_links[j],post_texts,post_names)

        
driver.quit()

data = {
    "Name": post_names,
    "Content": post_texts,
} 
df = pd.DataFrame(data)
df.to_csv("gtesting2.csv", encoding='utf-8', index=False)
writer = pd.ExcelWriter("gtesting2.xlsx", engine='xlsxwriter')
df.to_excel(writer, index =False)
writer.close()

df.to_csv("test1.csv", encoding='utf-8', index=False)

