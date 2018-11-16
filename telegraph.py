# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 16:08:30 2018

@author: AkSangwan
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


# method for telegraph.co.uk/business text scraping
def telegraph(Company):
    
    Punc_removed_text=''
    html = None
    news_link=[]
    news_summary=[]
    # check if website url is accessible
    try:    
       html = urlopen('https://www.telegraph.co.uk/business/').read()
    except:
       print('#1 Telegraph url open fail')
    headings=[]
    link=[]
    
    #chekc for html content and get soup object
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
    
    
    #getting all the elevant headings and corresponding url from webpage
    if soup is not None:
        try:
            Main_heading = soup.find('div', class_='splitter section').find_all('h3', class_='list-of-entities__item-body-headline')
        except:
            print("#2 Telegraph Main heading scraping error")
        try:
            Section_2 = soup.find('section', class_='p_hub__section_2 container').find_all('h3', class_='list-of-entities__item-body-headline')
        except:
            print("#3 Telegraph section 2 scraping error")
        try:
            Third_Block = soup.find('div', class_='splitter component splitter__1-1-1').find_all('h3', class_='list-of-entities__item-body-headline')
        except:
            print("#4 Telegraph Third block scraping error")
    
                       
    news_category_list = [Main_heading,Section_2,Third_Block]       
    
    #get link and heading by scraping page under the relevant html tags
    for list_type in news_category_list:
        for x in list_type:
            url =x.findAll(href=re.compile("/business"))
            if len(url) == 0:
                url =x.findAll(href=re.compile("/connect"))
            if len(url) == 0:
                url =x.findAll(href=re.compile("/investing"))
            if len(url) == 0:
                url =x.findAll(href=re.compile("/technology"))
            if len(url)>0:
                url_link = url[0]
                final_url =url_link.get('href') 
                final_url = 'https://www.telegraph.co.uk'+ final_url
                link.append(final_url)
                #if url found then only append heading to headings list
                text = re.sub('<[^>]+>','', str(x))
                text = text.strip()
                headings.append(str(text))
           
    CompanyName = Company.lower()
    News_list=[]
    
    #check if we have collected any headings and urls to open   
    if (len(headings)>0 and len(link)>0):
      for indx in range(len(headings)):
        if(CompanyName in headings[indx].lower()): 
            
          news_html = None
          news_text =''
          Punc_removed_text = ''
          
          try:
             news_html = urlopen(link[indx]).read()
             
          except:
             print('#5 Telegraph loop url open fail')
                   
          #finding all the text under the opened url
          news_text =""
          if news_html is not None:
              news_html_soup = BeautifulSoup(news_html, 'html.parser')
              try:
                news_text = news_html_soup.find('div', class_='articleBodyText section version-2').find_all('p')
              except:
                 try:
                     news_text = news_html_soup.find('div', class_='articleBodyText version-2 section').find_all('p')
                 except:
                     print("#6 Telegraph Error")
          
              if ( "" != news_text):
                     #cleaning text data
                     #removing all tag marks as well as punctuations from text
                     news_text = re.sub('<[^>]+>','', str(news_text))
                     Punc_removed_text = re.sub(r'[^\w\s]','',news_text)
                     News_list.append(Punc_removed_text)
                     news_link.append(link[indx])
                     news_summary.append(headings[indx])
              #print((Punc_removed_text))


    return News_list,news_link,news_summary

#get the output from the method to do sentiment analytics in AWS Comprehend eventually
