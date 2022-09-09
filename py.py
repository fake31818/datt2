import sys
sys.stdout.write('\r'+ "Starting... 1/4")
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import shutil
import time
import os
sys.stdout.write('\r'+ "Starting... 2/4")
url_file = str(os.environ['url2file'])
name_file = str(os.environ['name2file'])
option_url = os.environ['option2url']
patchfile = os.getcwd()
sys.stdout.write('\r'+ "Starting... 3/4")
#------------------------------------------------------------------------------------
print(url_file)
print(name_file)
sys.stdout.write('\r'+ "Starting... 4/4")
if(option_url == "1"):
    os.system("curl " + url_file + " --output "+ name_file) 
elif(option_url == "2"):
    os.system("mega-get " + url_file)
    print("M Done!")
#------------------------------------------------------------------------------------
sys.stdout.write('\r'+ "Loading... 0/4")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
sys.stdout.write('\r'+ "Loading... 1/4")
driver.get("https://trainbit.com/membership/login.aspx")
sys.stdout.write('\r'+ "Loading... 2/4")
driver.find_element(by=By.ID,value="ctl00_ContentPlaceHolder1_t_email").send_keys("moym8414@gmail.com")
driver.find_element(by=By.ID,value="ctl00_ContentPlaceHolder1_t_password").send_keys("09162828")
driver.find_element(by=By.ID,value="ctl00_ContentPlaceHolder1_b_login").click()
sys.stdout.write('\r'+ "Loading... 3/4")
driver.get("https://trainbit.com/files/")
time.sleep(4)
sys.stdout.write('\r'+ "Loading... 4/4")
driver.find_element(by=By.ID,value="f_upload").send_keys(patchfile + "/" + name_file)
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li/div/p[2]/span")))
number = driver.find_elements(by=By.XPATH,value="/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li/div/p[2]/span")
print("\n" + name_file)
num = True
while num == True:
    for elt in number:
        x = elt.text
        xu = x.replace("%", "")
        elt2 = int(xu)
        if(elt2 > 10 and elt2 < 12):print(elt.text)
        if(elt2 > 25 and elt2 < 27):print(elt.text)
        if(elt2 > 50 and elt2 < 55):print(elt.text)
        if(elt2 > 75 and elt2 < 77):print(elt.text)
        if(elt2 > 90 and elt2 < 95):print(elt.text)
        if(elt2 > 99):
            num = False
    time.sleep(0.1)
time.sleep(1)
print("100%")	
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li")))
time.sleep(8)
print("Upload Done! :D")
