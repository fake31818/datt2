import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import shutil
import time
import os
import sys
from tqdm.auto import tqdm
url_file = os.environ['url2file']
url_mega_1 = os.environ['url2mega_1']
url_mega_2 = os.environ['url2mega_2']
option_url = os.environ['option2url']
patchfile = os.getcwd()
#------------------------------------------------------------------------------------
if(option_url == "1"):
    with requests.get(url_file, stream=True) as r:
        
        total_length = int(r.headers.get("Content-Length"))
        
        with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
        
            # save the output to a file
            with open(name_file, 'wb')as output:
                shutil.copyfileobj(raw, output)
elif(option_url == "2"):
    os.system("mega-get " + url_file)
    print("Mega Done!")
if(url_mega_1 != "no"):
    os.system("mega-get " + url_mega_1)
    print("Mega Done!")
if(url_mega_2 != "no"):
    os.system("mega-get " + url_mega_2)
    print("Mega Done!")
#------------------------------------------------------------------------------------
sys.stdout.write('\r'+ "Loading... 0/4")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
def mega_name():
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[2]/div[2]/section/div[1]/div/div[4]/div[3]/div[1]/div[1]")))
    time.sleep(3)
    name_file_mega = driver.find_elements(by=By.XPATH,value="/html/body/div[6]/div[2]/div[2]/section/div[1]/div/div[4]/div[3]/div[1]/div[1]")
    for nf in name_file_mega:
        name_file = nf.get_attribute("title")
    tup(name_file)

def tup(name_file):
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
    print("\n" + name_file)
    num = True
    while num == True:
        try:
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li")))
            break
        except:
            pass
         
    time.sleep(1)
    print("100%")
    time.sleep(5)
    print("Upload Done! :D")
    driver.close()

if(option_url == "2"):
    driver.get(url_file)
    mega_name()
if(url_mega_1 != "no"):
    driver.get(url_mega_1)
    mega_name()
if(url_mega_2 != "no"):
    driver.get(url_mega_2)
    mega_name()
print("------------")
