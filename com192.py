# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 12:21:48 2018

@author: AkSangwan
"""

# -----------------------------------------------------------------------------------
# ----------------------imports---------------------
# -----------------------------------------------------------------------------------

from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from http.cookiejar import CookieJar


# url = 'https://www.192.com/'


# -----------------------------------------------------------------------------------
# ----------------------com192---------------------
# -----------------------------------------------------------------------------------


def com192(CompanyName, PinCode):
    driver = webdriver.Chrome()
    # chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--log-level=3')
    # chrome_options.add_argument('headless')
    driver.get("https://www.192.com/businesses/search/")
    # driver.maximize_window()
    time.sleep(4)

    # Find form to log in
    name = driver.find_element_by_id("businessesLookingFor")
    pincode = driver.find_element_by_id("businessesLocation")

    name.send_keys(CompanyName)
    pincode.send_keys(PinCode)
    name.submit()
    time.sleep(4)
    # url =driver.current_url

    # html = urlopen(url)
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    phone_soup = soup.find('div', class_='phoneCol')
    # print(heading_html)
    Phone_number = re.sub('<[^>]+>', '', str(phone_soup))
    Phone_number = Phone_number.strip()
    Phone_number = Phone_number.replace(" ", "")

    driver.close()

    return Phone_number

# -----------------------------------------------------------------------------------
# ----------------------xxxxxxxxxxxxxxxxxxxxxxxxxx---------------------
# -----------------------------------------------------------------------------------
