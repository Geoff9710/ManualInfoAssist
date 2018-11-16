# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:10:13 2018

@author: AkSangwan
"""



from bs4 import BeautifulSoup
from urllib.request import urlopen
import re



# method for https://www.multimodal.org.uk/news text scraping
def PR_newswire_news(Company):

    Punc_removed_text=''
    html = None
    soup = None
    news_link=[]
    news_summary=[]
    
    # check if website url is accessible
    try:    
      html = urlopen('http://www.prnewswire.co.uk/news-releases/news-releases-list/?page=1&pagesize=100').read()
    except:
      print('#1 PRnews2 url open fail')
      
    headings=[]
    link=[]
    paragraphs=[]
    
    #chekc for html content and get soup object
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
    heading_html = None
    para_html = None
    
    #getting all the elevant headings and corresponding url from webpage
    if soup is not None:
        try:
            heading_html = soup.find('div', class_='col-sm-8 card-list-hr card-list').find_all('h3')
        except:
            print("#2 PRnews2 heading_html scraping error")
            
        try:
            para_html = soup.find('div', class_='col-sm-8 card-list-hr card-list').find_all('p')
        except:
            print("#3 PRnews2 para_html scraping error")
            
            
    for indx in heading_html:
        url =indx.findAll(href=re.compile("http://"))
        #print(url)
        if len(url)>0:
            #Get all the urls from the html tag h3
            url_link= url[0]
            final_url =url_link.get('href') 
            link.append(final_url)
            
            #Get all the headings
            title = url_link.get('title')
            headings.append(str(title))
            
    for indx in para_html:
        para = re.sub('<[^>]+>','', str(indx))
        paragraphs.append(str(para))
        
    

    #convert company name to loer case for good match
    CompanyName = Company.lower()
    News_list=[]
    #check if we have collected any headings and urls to open
    if (len(headings)>0 and len(link)>0):
        
      for indx in range(len(headings)):
        
        if( CompanyName in headings[indx].lower() or CompanyName in paragraphs[indx].lower()):
          news_html = None
          news_text =''
          Punc_removed_text = ''
          
          try:
             news_html = urlopen(link[indx]).read()
             
          except:
             print('#4 PRnews2 loop url open fail')
          
          #finding all the text under the opened url
          if news_html is not None:
              news_html_soup = BeautifulSoup(news_html, 'html.parser')
              try:
                  
                  news_text = news_html_soup.find('article', class_='news-release carousel-template').find_all('p')
                  #print(news_html_soup)
              except:
                  print("#5 PRnews2 news_text scraping error")
              
              #cleaning text data
              #removing all tag marks as well as punctuations from text
              if ( "" != news_text):
                  news_text = re.sub('<[^>]+>','', str(news_text))
                  Punc_removed_text = re.sub(r'[^\w\s]','',news_text)
                  News_list.append(Punc_removed_text)
                  news_link.append(link[indx])
                  news_summary.append(headings[indx])
                  print((Punc_removed_text))
                    
     #Later:: Add another loop for adding text from all relevant news in one object

  
    return News_list,news_link,news_summary
        
