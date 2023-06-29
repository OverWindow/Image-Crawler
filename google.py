from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
import shutil

#### 개발자 툴 ####
searchItem = "김민재"
howMany = 5
# 실행방법: python google.py
# 실행 중 뜨는 오류들은 무시하시면 됩니다
###################

try:
    os.mkdir(searchItem)
except:
    shutil.rmtree(searchItem)
    os.mkdir(searchItem)

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys(searchItem)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height


imgs = driver.find_elements(By.CSS_SELECTOR,'.rg_i.Q4LuWd')
count = 1
for img in imgs:
    try: 
        if(img):
            img.click()
        else:
            print("no images")
        time.sleep(2)
        imgUrl = img.get_attribute("src")
        dst = f"{searchItem}/{count:03}.jpg"
        urllib.request.urlretrieve(imgUrl, dst)
        count += 1
    except:
        pass
    if(count == howMany+1):
        break

driver.close()

### 안 쓰는 코드 ###
# assert "Python" in driver.title
# assert "No results found." not in driver.page_source