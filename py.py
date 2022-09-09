import sys
import os
print("Starting....")
os.system("wget https://mega.nz/linux/repo/Debian_9.0/amd64/megacmd-Debian_9.0_amd64.deb")
os.system("sudo apt install ./megacmd-Debian_9.0_amd64.deb")
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import shutil
import time
url_file = os.environ['url2file']
name_file = os.environ['name2file']
option_url = os.environ['option2url']
option_url = str(option_url)
#------------------------------------------------------------------------------------
print(url_file)
print(name_file)
if(option_url == "1"):
    name_file = name_file.replace(" ","-")
    try:
        r = requests.get(url_file)
        with open(name_file,'wb') as f:
            f.write(r.content)
    except:
        os.system(f'curl "{url_file}" --output "{name_file}"') 
if(option_url == "2"):
    os.system("mega-get " + url_file)
    print("M Done!")
#------------------------------------------------------------------------------------
sys.stdout.write('\r'+ "Loading... 0/4")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
print("Loading... 1/4")
driver.get("https://trainbit.com/membership/login.aspx")
print("Loading... 2/4")
driver.find_element(by=By.ID,value="ctl00_ContentPlaceHolder1_t_email").send_keys("moym8414@gmail.com")
driver.find_element(by=By.ID,value="ctl00_ContentPlaceHolder1_t_password").send_keys("09162828")
driver.find_element(by=By.ID,value="ctl00_ContentPlaceHolder1_b_login").click()
print("Loading... 3/4")
driver.get("https://trainbit.com/files/")
time.sleep(1)
print("Loading... 4/4")
driver.find_element(by=By.ID,value="f_upload").send_keys("./" + name_file)
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li/div/p[2]/span")))
number = driver.find_elements(by=By.XPATH,value="/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li/div/p[2]/span")
print("\n" + name_file)
num = True
while num == True:
    for elt in number:
        x = elt.text
        xu = x.replace("%", "")
        elt2 = int(xu)
        if(elt2 >= 98):
            print("%" + str(elt2))
            num = False
    time.sleep(0.1)
time.sleep(1)
print("100%")	
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li")))
time.sleep(6)
print("Upload Done! :D")
