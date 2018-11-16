# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:52:16 2018

@author: AkSangwan
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


# method for constructionenquirer.com text scraping
def bbc_uk(Company):
    Punc_removed_text = ''
    news_link = []
    news_summary = []
    html = None
    try:
        html = urlopen('https://www.bbc.co.uk/news/business').read()
    except:
        print('#1 BBC url open fail')

    headings = []
    link = []
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
    Main_heading = []
    Second_Block = []
    Third_Block = []
    if soup is not None:
        try:
            Main_heading = soup.find('div', class_='distinct-component-group container-buzzard').find_all('a',
                                                                                                          class_='title-link')
        except:
            print("#2 bbc main heading scraping error")
        try:
            Second_Block = soup.find('div', class_='distinct-component-group container-pigeon').find_all('a')
        except:
            print("#3 bbc second block scraping error")
        try:
            Third_Block = soup.find('div', class_='distinct-component-group container-macaw').find_all('a')
        except:
            print("#4 bbc third block scraping error")

    mylist = [Main_heading, Second_Block, Third_Block]

    for indx in mylist:
        for x in indx:
            y = x.get('href')
            y = 'https://www.bbc.co.uk' + y
            link.append(y)
            text = re.sub('<[^>]+>', '', str(x))
            text = text.strip()
            headings.append(str(text))

    CompanyName = Company.lower()

    News_list = []
    if (len(headings) > 0 and len(link) > 0):
        for indx in range(len(headings)):
            if (CompanyName in headings[indx].lower()):
                news_text = ""
                news_html = None
                try:
                    news_html = urlopen(link[indx]).read()

                except:
                    print('#5 BBC loop url open fail')

                # finding all the text under the opened url

                if news_html is not None:
                    news_html_soup = BeautifulSoup(news_html, 'html.parser')
                    try:
                        news_text = news_html_soup.find('div', class_='story-body').find_all('p')
                    except:
                        print("#6 bbc news_text error")

                    # cleaning text data
                    # removing all tag marks as well as punctuations from text
                    if ("" != news_text):
                        news_text = re.sub('<[^>]+>', '', str(news_text))
                        Punc_removed_text = re.sub(r'[^\w\s]', '', news_text)
                        News_list.append(Punc_removed_text)
                        news_link.append(link[indx])
                        news_summary.append(headings[indx])
                    # print((Punc_removed_text))
    # print((Punc_removed_text))
    # end of method

    return News_list, news_link, news_summary

# get the output from the method to do sentimental analytics in AWS Comprehend eventually

