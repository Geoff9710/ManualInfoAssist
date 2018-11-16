# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:38:31 2018

@author: AkSangwan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:18:24 2018

@author: AkSangwan
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


# method for news.sky.com/business text scraping
def sky_news(Company):
    
    Punc_removed_text =''
    html = None
    news_link=[]
    news_summary = []
    # check if website url is accessible
    try:    
       html = urlopen('https://news.sky.com/business').read()
    except:
       print('#1 Sky News url open fail')
    
    headings=[]
    link=[]
    heading_field = None
    trending = None
    more_news = None
    soup = None
    #chekc for html content and get soup object
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
    if soup is not None:
        try:
            heading_field = soup.find('div', class_='site-main').find_all('h3', class_='sdc-news-story-grid__headline')
        except:
            print("#2 Sky News heading field scraping error")
        try:
           more_news = soup.find('div', id='component-top-stories-secondary').find_all('h3', class_='sdc-news-story-grid__headline')
        except:
           print("#3 Sky News more_news scraping error")
        try:
           trending = soup.find('div', id='component-trending').find_all('a')
        except:
           print("#4 Sky News Trending news scraping error")
        
    
    #put following two code paras in one, use list of fields

    for x in heading_field:
           #first get the url link of this heading and save in a list
           url =x.findAll(href=re.compile("/story"))
           if len(url)>0:
               url_link= url[0]
               final_url =url_link.get('href') 
               final_url = 'https://news.sky.com/'+ final_url
               link.append(final_url)
            
           #filter the heading text and save it in headings list 
           text = re.sub('<[^>]+>','', str(x))
           headings.append(str(text))
           
    for x in more_news:
           #first get the url link of this heading and save in a list
           url =x.findAll(href=re.compile("/story"))
           if len(url)>0:
               url_link = url[0]
               final_url =url_link.get('href') 
               final_url = 'https://news.sky.com/'+ final_url
               link.append(final_url)
            #filter the heading text and save it in headings list
            
           text = re.sub('<[^>]+>','', str(x))
           headings.append(str(text))
           

    for x in trending:
           y =x.get('href') 
           y = 'https://news.sky.com/'+y
           link.append(y)
           text = re.sub('<[^>]+>','', str(x))
           text = text.strip()
           headings.append(str(text))
    

    #convert company name to loer case for good match
    CompanyName = Company.lower()
    News_list=[]
    #check if we have collected any headings and urls to open
    if (len(headings)>0 and len(link)>0):
        
      for indx in range(len(headings)):
        if( CompanyName in headings[indx].lower()):
          
          news_html = None
          news_text =''
          Punc_removed_text = ''
          
          
          try:
             news_html = urlopen(link[indx]).read()
             
          except:
             print('#5 Sky News loop url open fail')
          
          #finding all the text under the opened url
          if news_html is not None:
              news_html_soup = BeautifulSoup(news_html, 'html.parser')
              try:
                  news_text = news_html_soup.find('div', class_='sdc-news-story-article__body').find_all('p')
              except:
                  print("#6 Sky News news_text scraping error")
        
              #cleaning text data
              #removing all tag marks as well as punctuations from text
              if ( "" != news_text):
                  news_text = re.sub('<[^>]+>','', str(news_text))
                  Punc_removed_text = re.sub(r'[^\w\s]','',news_text)
                  News_list.append(Punc_removed_text)
                  news_link.append(link[indx])
                  news_summary.append(headings[indx])
                  #print((Punc_removed_text))
                    
     #Later:: Add another loop for adding text from all relevant news in one object
    
    
    return News_list,news_link, news_summary
 
#get the output from the method to do sentimental analytics in AWS Comprehend eventually
    

