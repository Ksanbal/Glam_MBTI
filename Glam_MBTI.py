from CatHand import CatHandBot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from itertools import product
import time
import re
import csv
import os
import traceback

# Firefox Driver
opts = webdriver.FirefoxOptions()
opts.add_argument('Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:83.0) Gecko/20100101 Firefox/83.0')
opts.add_argument("--headless")
driver = webdriver.Firefox(executable_path='./geckodriver', options=opts)

# 중복순열
test = list(product([1,2], repeat=12))

# 이미 넣어본 값은 건너뛰기
with open('result.csv', 'r') as f:
    l = len(f.readlines())
test = test[l:]

# 크롤링 코드
def getMBTI():
    try:
        for i in test:
            test_list = list(i)
            driver.get('http://16types.glam.am/test')

            for t in test_list:
                time.sleep(1.5)
                btns = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'option__1OU7l')))
                btns = driver.find_elements_by_class_name('option__1OU7l')
                if t == 1:
                    btns[0].click()
                else:
                    btns[1].click()

            result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'type__23j8y'))).text
            with open('result.csv', 'a') as f:
                csv.writer(f).writerow(test_list+[result])
        return (True, '드디어 끝났업')
    except Exception:
        return (False, f'에러 났따아...\n*****\nError\n{traceback.format_exc()}\n*****')

temp_result = getMBTI()
driver.quit()

if temp_result[0]:
    CatHandBot.sendTalk(temp_result[1])
else:
    CatHandBot.sendTalk(temp_result[1])