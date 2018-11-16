# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:22:00 2018

@author: AkSangwan
"""


#-----------------------------------------------------------------------------------
#-------------------------------IMPORT MODULES--------------------------------------
#-----------------------------------------------------------------------------------
import feedparser
from fpdf import FPDF


#-----------------------------------------------------------------------------------
#---------------------------PRINT THE RESULTS IN PDF--------------
#----------------------------------------------------------------------------------
def print_pdf(CompanyName, title_list, link_list):
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(ln = 1, h=5.0, align='L', w=0, txt= CompanyName.upper(), border=0)

    for indx in range(len(title_list)):
        pdf.ln(1)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(10)
        pdf.multi_cell(h=5.0, align='L', w=0, txt= 'Headline: ' + title_list[indx], border=0)

        pdf.ln(0)
        pdf.set_font('Arial', '', 12)
        pdf.cell(10)
        pdf.multi_cell(h=5.0, align='L', w=0, txt= 'Source url: ' + link_list[indx], border=0)

        pdf.ln(0)
        pdf.cell(10)
        pdf.multi_cell(h=0.25, align='L', w=0, txt= '', border=1, fill= 1)
        pdf.ln(0)

    pdf.output('RSS_pdf.pdf', 'F')
        

    
    return True



def RSS_feedScraping(Company):
    #-------------------------------RSS FILE SOURCE--------------
    #description=[]
    title=[]
    link=[]
    New_title_list=[]
    New_link_list=[]
    with open("URL_text_file.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    #------------------------------PARSE THE DATA--------------

    for indx in range(len(content)):
        url = content[indx]
    
        #using feedparser to parse rss feed pages
        parsedFeed = feedparser.parse(url)
        for feed in parsedFeed.entries:
            #description_news =feed.description
            #description.append(description_news)
        
            title_news = feed.title
            title.append(title_news)
        
            link_news = feed.link
            link.append(link_news)



    #-------------------------SEARCH NEWS RELATED TO COMPANY--------------

    if len(title) == len(link): #and len(link) == len(description):
        for indx in range(len(title)):
           if CompanyName in title[indx].lower():
               New_title_list.append(title[indx])
               New_link_list.append(link[indx])
           
    print('No of Results found: ', len(New_title_list))


#---------------------------CHECKS BEFORE PRINTING PDF--------------

    if 0 != len(New_title_list) and (len(New_title_list) == len(New_link_list)):
        print_pdf(CompanyName, New_title_list, New_link_list)
    
    
    return True
    
    
    
#-----------------------------------------------------------------------------------
#--------------------------------main-----------------------------------------------
#-----------------------------------------------------------------------------------
CompanyName = input("Enter the company name: ")
CompanyName = CompanyName.lower()


#call RSS_feedScraping to parse and print fees from url taken from an .txt file
RSS_feedScraping(CompanyName)

#-----------------------------------------------------------------------------------
#-------------------------------------END-------------------------------------------
#-----------------------------------------------------------------------------------
    
    
    
    
    
    
    
    
    
    
    
    
    