# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:54:22 2018

@author: AkSangwan
"""

#-----------------------------------------------------------------------------------
#-------------------------------------imports------------------------------------------
#-----------------------------------------------------------------------------------


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


#-----------------------------------------------------------------------------------
#--------------------------------more_news_page_SCRAP-------------------------------
#-----------------------------------------------------------------------------------



def more_news_page(soup):
    
    More_news_link = None
    
    try:
        More_news_link = soup.find('div', class_='moreLink').find_all('a')
    except:
        print("#2 Reuters More_news_link scraping error")
                  
                 
    if More_news_link is not None:
        url = More_news_link[0].get('href')
    More_news_url = 'https://uk.reuters.com'+url
    
    morenews_heading= None
    morenews_para = None
    
    html = None
    headings=[]
    links=[]
    paragraphs=[]
    if (len(More_news_url)>0):
        for i in range(5):
           url = More_news_url+ '&page=' + str(i) + '&pageSize=10'
           if len(url)>0:
              
              try:    
                 html = urlopen(url).read()
              except:
                 print('#1.1 Reuters url open fail')
           if html is not None:
              soup = BeautifulSoup(html, 'html.parser')

           if soup is not None:
              try:
                  morenews_heading = soup.find('div', class_='news-headline-list').find_all('div', class_= 'story-content')
              except:   
                  print("#1.2 Reuters morenews_heading scraping failed")
              try:
                  morenews_para = soup.find('div', class_='news-headline-list').find_all('p')
              except:
                  print('#1.3 Reuters morenews_para scraping failed')

        #print((morenews_heading[3]))

        #print((morenews_para[3]))
           if morenews_heading is not None:
               for x in morenews_heading:
                  y =x.find_all('a') 
                  #print((y[0]))
                  y = y[0].get('href')
                  y = 'https://uk.reuters.com'+str(y)
                  links.append(y)
                  #print(str(y[0]))
                  z = x.find_all('h3', class_='story-title')
                  text = re.sub('<[^>]+>','', str(z[0]))
                  text = text.strip()
                  headings.append(str(text))
                  #headings.append(str(text))
                  #print(text)
           if morenews_para is not None:
               for x in morenews_para:
                  y = re.sub('<[^>]+>','', str(x))
                  paragraphs.append(y)
    
    return headings, links, paragraphs

#-----------------------------------------------------------------------------------
#----------------------------main_heading_scrap-------------------------------------
#-----------------------------------------------------------------------------------
    


def main_heading_scrape(soup, Company):
    
    headings=[]
    link=[]
    paragraphs=[]
    columnLeft = None
    columnLeftP = None
    

    if soup is not None:
        try:
            columnLeft = soup.find('div', class_='columnLeft').find_all('h2')
        except:
            print("#2 Reuters column_left scraping error")
        
        try:
            columnLeftP = soup.find('div', class_='columnLeft').find_all('p')
        except:
            print("#3 Reuters column_leftP scraping error")
                  
        
    
    
    if len(columnLeft)>0:
        y =columnLeft[0].findAll(href=re.compile("/article"))
        h1 = columnLeft[0]
        head1 = re.sub('<[^>]+>', '', str(h1))
        headings.append(head1)
    if len(y)>0:
        y =y[0].get('href') 
        y = 'https://uk.reuters.com'+y
        link.append(y)
    #print (y)
    #h1 = columnLeft[0]
    #head1 = re.sub('<[^>]+>', '', str(h1))
    #print(head1)
    if len(columnLeftP)>0:
        p1 = columnLeftP[0]
        para1 = re.sub('<[^>]+>', '', str(p1))
        paragraphs.append(para1)
            
    return headings,link,paragraphs



#-----------------------------------------------------------------------------------
#--------------------------more_business_news_scrap---------------------------------
#-----------------------------------------------------------------------------------



def more_business_news_scrape(soup):
    
    headings = []
    paragraphs = []
    link =[]
    # Scraping the MORE BUSINESS NEWS section   
    if soup is not None:
        try:
            moreSectionNews = soup.find('div', class_='more-section-news-top gridPanel grid8').find_all('h2')
            
        except:
            print("#5 Reuters moreSectionNews scraping error")
            
        try:
            moreSectionNewsP = soup.find('div', class_='more-section-news-top gridPanel grid8').find_all('p')
        except:
            print("#6 Reuters moreSectionNewsP scraping error")
    

    #get the headings and the url link
    for x in moreSectionNews:
        head = re.sub('<[^>]+>', '', str(x))
        headings.append(str(head))
        y = (x.findAll('a', attrs={'href': re.compile("/article")}))
        if (len(y)>0):
            url = y[0].get('href')
            url = 'https://uk.reuters.com'+ url
            link.append(str(url))
    
    #get the paragraphgs content         
    for x in moreSectionNewsP:
        para = re.sub('<[^>]+>', '', str(x))
        paragraphs.append(str(para))
    
    
    return headings,link,paragraphs




#-----------------------------------------------------------------------------------
#-----------------------------uk_reuters--------------------------------------------
#-----------------------------------------------------------------------------------
# method for uk.reuters.com/business text scraping


def uk_reuters(Company):
    
    Punc_removed_text=''
    html = None
    news_link=[]
    news_summary =[]
    soup = None
    
    try:    
       html = urlopen('https://uk.reuters.com/business').read()
    except:
       print('#1 Reuters url open fail')
    
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
    
    
    
    more_news_50_headings=None
    more_news_50_links=None
    more_news_50_paragraphs=None
    if soup is not None:
        more_news_50_headings, more_news_50_links, more_news_50_paragraphs = more_news_page(soup)
        
    if soup is not None:
        main_heading, main_heading_url,main_heading_para = main_heading_scrape(soup,Company)

      
    if soup is not None:
        more_business_heading, more_business_url, more_business_paragraph = more_business_news_scrape(soup)
    
    

    CompanyName = Company.lower()
    
    
    list_heading=[]
    list_link=[]
    list_paragraph=[]
    
    
    for i in range(len(main_heading)):
        list_heading.append(main_heading[i])
        list_link.append(main_heading_url[i])
        list_paragraph.append(main_heading_para[i])
        
    for i in range(len(more_news_50_headings)):
        list_heading.append(more_news_50_headings[i])
        list_link.append(more_news_50_links[i])
        list_paragraph.append(more_news_50_paragraphs[i])
        
    for i in range(len(more_business_heading)):
        list_heading.append(more_business_heading[i])
        list_link.append(more_business_url[i])
        list_paragraph.append(more_business_paragraph[i])
  

        
    News_list =[]
    
    #check if we have collected any headings and urls to open
    if (len(list_heading)>0 and len(list_paragraph)>0 and len(list_link)>0):
      
      for indx in range(len(list_paragraph)):
        if( CompanyName in list_heading[indx].lower() or CompanyName in list_paragraph[indx]):

          try:
             news_html = urlopen(list_link[indx]).read()
             
          except:
             print('#7 Reuters loop url open fail')
             
          news_html_soup = BeautifulSoup(news_html, 'html.parser')
          if news_html_soup is not None:
              try:
                  news_text = news_html_soup.find('div', class_='StandardArticleBody_body').find_all('p')
              except:
                  print("#8 Reuters Couldn't find news text")
          #find content from url and save all the relevant text for further sentiment analysis
          
              if ( "" != news_text):
                  news_text = re.sub('<[^>]+>','', str(news_text))
                  Punc_removed_text = re.sub(r'[^\w\s]','',news_text)
                  News_list.append(Punc_removed_text)
                  news_link.append(list_link[indx])
                  news_summary.append(list_heading[indx])
                  

    
    return News_list,news_link, news_summary
 
    

#-----------------------------------------------------------------------------------
#---------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-------------------------
#-----------------------------------------------------------------------------------
    










