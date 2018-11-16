# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 17:19:21 2018

@author: AkSangwan
"""


#-----------------------------------------------------------------------------------
#----------------------imports---------------------
#-----------------------------------------------------------------------------------
from selenium import webdriver


import re
import time
from bs4 import BeautifulSoup


#url = 'https://www.192.com/'



#-----------------------------------------------------------------------------------
#----------------------com192---------------------
#-----------------------------------------------------------------------------------
def thomsonLocal(CompanyName, PinCode):
    driver = webdriver.Chrome()
    #chrome_options = webdriver.ChromeOptions()


    driver.get("https://www.thomsonlocal.com/")
    #driver.maximize_window()
    time.sleep(4)
        
    # Find form to log in
    
    name=driver.find_element_by_id("whatSearchHome")
    pincode=driver.find_element_by_id("homeWhereSearch")
    
    name.send_keys(CompanyName)
    pincode.send_keys(PinCode)
    name.submit()
    time.sleep(4)


    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    
    phone_soup =soup.find('div', class_='phoneCont blue1BG mobileHide')
    #print(heading_html)
    Phone_number = re.sub('<[^>]+>','', str(phone_soup))
    Phone_number = Phone_number.strip()
    Phone_number = Phone_number.replace(" ","")

    driver.close()
    
    return Phone_number




#-----------------------------------------------------------------------------------
#----------------------xxxxxxxxxxxxxxxxxxxxxxxxxx---------------------
#-----------------------------------------------------------------------------------
    


'''
import requests

#url = "http://www.tradegate.de/orderbuch.php?isin=CH0012138530"

r = requests.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}, timeout=15)
print(r.content)
'''
'''
import urllib
from urllib.request import Request

req = urllib.request.Request(url, None, {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})
cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.open(Request(req, headers={'User-Agent': 'Mozilla'}))
#html = opener.open(req)
#print(html)
#soup = BeautifulSoup(html, 'html.parser')
#print(soup)
#phone = soup.find('div', class_='').find_all('h3')
'''

'''

import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

#url = "http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers"
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() '''
