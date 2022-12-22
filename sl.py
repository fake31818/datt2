from IPython.display import clear_output
import time , os , sys, tqdm, re
try:from selenium import webdriver
except:
  print("instaling...")
  os.system("pip install selenium;sudo apt-get install chromium-chromedriver -y")
  from selenium import webdriver
  print("installed!")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#------------------------------------------------------------------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
URL = "https://slwatch.co/v/7vjPWlqKKR1D34JK"
if URL == "":
  print("URL Empty!")
  exit()
driver.get(URL)
url = driver.find_elements(by=By.XPATH,value='//*[@id="downloadCollapse"]/div/a')
filesize_MB= "1230"
filesize=int(filesize_MB)
pbar = tqdm.tqdm(total=int(filesize),position=0,bar_format='{l_bar}{bar:50}{r_bar}{bar:-50b}')
clear_output()
print(str(filesize)+"MB")
url = url[0].get_attribute("href")
filename = str(driver.find_elements(by=By.XPATH,value='//*[@id="app"]/main/section/div/div/div[1]/h2')[0].text)+".crdownload"
print(filename)
try:os.remove(filename)
except:pass
OrgName = "an-imperfect-murder.mp4"
OrgName = OrgName.lower()
if OrgName == "":
  print("OrgName Empty!")
  exit()
print("File Name: "+OrgName)
driver.get(url)
time.sleep(3)
sb = 0
while True:
  try:
    s = (int(os.path.getsize(filename)) / 1024) / 1024
    per_down = int(s) - sb
    pbar.update(int(per_down))
    sb = int(s)
  except:
    try:
      filenamec = filename.replace(".crdownload","")
      os.path.getsize(filenamec)
      pbar.close()
      print("\nDownloaded!")
      driver.close()
      break
    except:pass
  time.sleep(1)


os.rename(filenamec, OrgName)
os.system(f"mega-put {OrgName}")
