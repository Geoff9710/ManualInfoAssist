# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:32:31 2018

@author: AkSangwan
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

'''
#checking the website availability, not relevant eventually as we have Used 'urlopen' API
site = requests.get('https://www.multimodal.org.uk/news', verify=False)
if site.status_code is 200:
    print('\n')
else:
    print("error code returned")
'''


# method for https://www.multimodal.org.uk/news text scraping
def multi_modal(Company):
    Punc_removed_text = ''
    html = None
    soup = None
    news_link = []
    news_summary = []
    # check if website url is accessible
    try:
        html = urlopen('https://www.multimodal.org.uk/news').read()
    except:
        print('#1 Multimodal url open fail')

    headings = []
    link = []

    # chekc for html content and get soup object
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')

    # getting all the elevant headings and corresponding url from webpage
    if soup is not None:
        try:
            heading_url = soup.find('div', class_='region region-content').find_all('a')
        except:
            print("#2 Multimodal heading_url scraping error ")

        try:
            Main_heading = soup.find('div', class_='region region-content').find_all('div', 'views-field-title')
        except:
            print("#3 Multimodal main heading scraping error")

    # getting all the href links and adding the default address to complete the url
    for x in heading_url:
        url = x.get('href')
        final_url = 'https://www.multimodal.org.uk' + url
        link.append(final_url)

    # the first and last link in result are irrelevant (website structure!!)
    if (len(link) > 0):
        del (link[0])
        z = len(link)
        del (link[z - 1])

    # getting tag information by removing <p> and similar tag marks
    for i in Main_heading:
        text = re.sub('<[^>]+>', '', str(i))
        headings.append(text)

    # convert company name to loer case for good match
    CompanyName = Company.lower()
    News_list = []
    # check if we have collected any headings and urls to open
    if (len(headings) > 0 and len(link) > 0):

        for indx in range(len(headings)):
            if (CompanyName in headings[indx].lower()):

                news_html = None
                news_text = ''

                try:
                    news_html = urlopen(link[indx]).read()

                except:
                    print('#4 Multimodal loop url open fail')

                # finding all the text under the opened url
                if news_html is not None:
                    news_html_soup = BeautifulSoup(news_html, 'html.parser')
                    try:
                        news_text = news_html_soup.find('div', class_='content').find_all('p')
                    except:
                        print("#5 Multimodal news_text scraping error")

                    # cleaning text data
                    # removing all tag marks as well as punctuations from text
                    if ("" != news_text):
                        news_text = re.sub('<[^>]+>', '', str(news_text))
                        Punc_removed_text = re.sub(r'[^\w\s]', '', news_text)
                        News_list.append(Punc_removed_text)
                        news_link.append(link[indx])
                        news_summary.append(headings[indx])
                        # print(Punc_removed_text)
    # end of method

    return News_list, news_link, news_summary

# get the output from the method to do sentimental analytics in AWS Comprehend eventually



