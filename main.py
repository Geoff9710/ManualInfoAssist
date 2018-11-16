# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:23:26 2018

@author: AkSangwan
"""

# -----------------------------------------------------------------------------------
# -------------------------------IMPORT MODULES--------------------------------------
# -----------------------------------------------------------------------------------

import Multimodal
import sky_news
import UKreuters
import telegraph
import Construction_Enquirer
import bbc_uk
import prnewswire
import prnewswire_news

import textwrap
import boto3

from fpdf import FPDF

# -----------------------------------------------------------------------------------
# --------------------AWS COMPREHEND CREDENTIALS-------------
# -----------------------------------------------------------------------------------


client = boto3.client(
    'comprehend', verify=False,
    region_name='us-east-1'
)


# -----------------------------------------------------------------------------------
# ----------------MULTIMODAL------------------------
# -----------------------------------------------------------------------------------
# Input is the Company name we are searching for
# returns list of all collected raw text, their url links and headlines
def webpage_scraping(Company):
    news_detailed_list = []
    news_link_list = []
    news_headline_list = []

    news_detailed_multimodal = []
    news_link_multimodal = []
    news_headline_multimodal = []

    # call the Multimodal module which returns scraping results
    news_detailed_multimodal, news_link_multimodal, news_headline_multimodal = Multimodal.multi_modal(Company)

    # making sure if length of list are equal which further ensures that all lists have matching corresponding content
    if ((len(news_detailed_multimodal) == len(news_link_multimodal)) and (
            len(news_headline_multimodal) == len(news_link_multimodal))):
        for indx in range(len(news_detailed_multimodal)):
            news_detailed_list.append(news_detailed_multimodal[indx])
            news_link_list.append(news_link_multimodal[indx])
            news_headline_list.append(news_headline_multimodal[indx])

    # -----------------------------------------------------------------------------------
    # ----------------SKY NEWS------------------------------
    # -----------------------------------------------------------------------------------
    news_detailed_skynews = []
    news_link_skynews = []
    news_headline_skynews = []

    news_detailed_skynews, news_link_skynews, news_headline_skynews = sky_news.sky_news(Company)

    if ((len(news_detailed_skynews) == len(news_link_skynews)) and (
            len(news_headline_skynews) == len(news_link_skynews))):
        for indx in range(len(news_detailed_skynews)):
            news_detailed_list.append(news_detailed_skynews[indx])
            news_link_list.append(news_link_skynews[indx])
            news_headline_list.append(news_headline_skynews[indx])

    # -----------------------------------------------------------------------------------
    # ----------------REUTERS----------------------
    # -----------------------------------------------------------------------------------
    news_detailed_reuters = []
    news_link_reuters = []
    news_headline_reuters = []

    news_detailed_reuters, news_link_reuters, news_headline_reuters = UKreuters.uk_reuters(Company)

    if ((len(news_detailed_reuters) == len(news_link_reuters)) and (
            len(news_headline_reuters) == len(news_link_reuters))):
        for indx in range(len(news_detailed_reuters)):
            news_detailed_list.append(news_detailed_reuters[indx])
            news_link_list.append(news_link_reuters[indx])
            news_headline_list.append(news_headline_reuters[indx])

    # -----------------------------------------------------------------------------------
    # --------------TELEGRAPH----------------------
    # -----------------------------------------------------------------------------------
    news_detailed_telegraph = []
    news_link_telegraph = []
    news_headline_telegraph = []

    news_detailed_telegraph, news_link_telegraph, news_headline_telegraph = telegraph.telegraph(Company)

    if ((len(news_detailed_telegraph) == len(news_link_telegraph)) and (
            len(news_headline_telegraph) == len(news_link_telegraph))):
        for indx in range(len(news_detailed_telegraph)):
            news_detailed_list.append(news_detailed_telegraph[indx])
            news_link_list.append(news_link_telegraph[indx])
            news_headline_list.append(news_headline_telegraph[indx])

    # -----------------------------------------------------------------------------------
    # -----------CONSTRUCTION ENQUIRER----------------------
    # -----------------------------------------------------------------------------------
    news_detailed_ConstructionEnquirer = []
    news_link_CE = []
    news_headline_CE = []

    news_detailed_ConstructionEnquirer, news_link_CE, news_headline_CE = Construction_Enquirer.construction_enquirer(
        Company)

    if ((len(news_detailed_ConstructionEnquirer) == len(news_link_CE)) and (
            len(news_headline_CE) == len(news_link_CE))):
        for indx in range(len(news_detailed_ConstructionEnquirer)):
            news_detailed_list.append(news_detailed_ConstructionEnquirer[indx])
            news_link_list.append(news_link_CE[indx])
            news_headline_list.append(news_headline_CE[indx])

    # -----------------------------------------------------------------------------------
    # ----------------BBC---------------------------------------
    # -----------------------------------------------------------------------------------

    news_detailed_BBC = []
    news_link_BBC = []
    news_headline_BBC = []

    news_detailed_BBC, news_link_BBC, news_headline_BBC = bbc_uk.bbc_uk(Company)

    if ((len(news_detailed_BBC) == len(news_link_BBC)) and (len(news_headline_BBC) == len(news_link_BBC))):
        for indx in range(len(news_detailed_BBC)):
            news_detailed_list.append(news_detailed_BBC[indx])
            news_link_list.append(news_link_BBC[indx])
            news_headline_list.append(news_headline_BBC[indx])

    # -----------------------------------------------------------------------------------
    # -------------PR_newswire_travel_and_leisure_100------------------
    # -----------------------------------------------------------------------------------
    news_detailed_PRnewswireTnL = []
    news_link_PRnewswireTnL = []
    news_headline_PRnewswireTnL = []

    news_detailed_PRnewswireTnL, news_link_PRnewswireTnL, news_headline_PRnewswireTnL = prnewswire.PR_newswire(Company)

    if ((len(news_detailed_PRnewswireTnL) == len(news_link_PRnewswireTnL)) and (
            len(news_headline_PRnewswireTnL) == len(news_link_PRnewswireTnL))):
        for indx in range(len(news_detailed_PRnewswireTnL)):
            news_detailed_list.append(news_detailed_PRnewswireTnL[indx])
            news_link_list.append(news_link_PRnewswireTnL[indx])
            news_headline_list.append(news_headline_PRnewswireTnL[indx])

    # -----------------------------------------------------------------------------------
    # -------------PR_newswire_news_release_list_100-------------------
    # -----------------------------------------------------------------------------------
    news_detailed_PRnewswireRL = []
    news_link_PRnewswireRL = []
    news_headline_PRnewswireRL = []

    news_detailed_PRnewswireRL, news_link_PRnewswireRL, news_headline_PRnewswireRL = prnewswire_news.PR_newswire_news(
        Company)

    if ((len(news_detailed_PRnewswireRL) == len(news_link_PRnewswireRL)) and len(news_headline_PRnewswireRL) == len(
            news_link_PRnewswireRL)):
        for indx in range(len(news_detailed_PRnewswireRL)):
            news_detailed_list.append(news_detailed_PRnewswireRL[indx])
            news_link_list.append(news_link_PRnewswireRL[indx])
            news_headline_list.append(news_headline_PRnewswireRL[indx])

    return news_detailed_list, news_link_list, news_headline_list


# -----------------------------------------------------------------------------------
# -----------------------------xxxxxxxxxxxxxx----------------------------------------
# -----------------------------------------------------------------------------------
# returns neutral, positive and negative sentiment scores of the news
# inputs are list of news raw text, url and headlines
def sentiment_score_calculation(news_detailed_list, news_link_list, news_headline_list):
    print(len(news_detailed_list))
    print(len(news_link_list))
    print(len(news_headline_list))

    sentiment_list = []
    positive_sentiment_score_list = []
    negative_sentiment_score_list = []
    neutral_sentiment_score_list = []
    mixed_sentiment_score_list = []

    for indx in range(len(news_detailed_list)):
        news_split_list = textwrap.wrap(news_detailed_list[indx], 4500, break_long_words=False)
        No_of_text_split = 0
        No_of_text_split = len(news_split_list)
        print('length of textwrap split is: ', No_of_text_split)

        score_Positive = 0
        score_Negative = 0
        score_Neutral = 0
        score_Mixed = 0
        sentiment = ''
        if No_of_text_split == 1:
            response = client.detect_sentiment(Text=news_split_list[0], LanguageCode='en')
            # print('Sentiment: ',response["Sentiment"])
            # print('Sentiment Score: ',response["SentimentScore"])

            sentiment = response["Sentiment"]
            score_Positive = response["SentimentScore"]["Positive"]
            score_Negative = response["SentimentScore"]["Negative"]
            score_Neutral = response["SentimentScore"]["Neutral"]
            score_Mixed = response["SentimentScore"]["Mixed"]

            print('Sentiment scores are:')
            print('Positive Sentiment Score: ', score_Positive)
            print('Negative Sentiment Score: ', score_Negative)
            print('Neutral Sentiment Score: ', score_Neutral)
            print('Mixed Sentiment Score: ', score_Mixed)
            print(news_link_list[indx])
            print(news_headline_list[indx])

        elif (No_of_text_split > 1):
            lenghth_of_last_textwrap = len(news_split_list[No_of_text_split - 1])

            for i in range(No_of_text_split - 1):
                # count = 0
                response = client.detect_sentiment(Text=news_split_list[i], LanguageCode='en')
                print('lenght of #', i + 1, ' split is: ', len(news_split_list[i]))
                # print('Sentiment: ',response["Sentiment"])
                # use wightage of each split to calculate scores
                score_Positive = score_Positive + response["SentimentScore"]["Positive"]
                score_Negative = score_Negative + response["SentimentScore"]["Negative"]
                score_Neutral = score_Neutral + response["SentimentScore"]["Neutral"]
                score_Mixed = score_Mixed + response["SentimentScore"]["Mixed"]

                # count = count + 1
            # score = lenghth_of_last_textwrap/4500

            W_response = client.detect_sentiment(Text=news_split_list[No_of_text_split - 1], LanguageCode='en')

            Weighted_Denominator = 4500 * (No_of_text_split - 1) + lenghth_of_last_textwrap

            score_Positive = (score_Positive * 4500 + lenghth_of_last_textwrap * (
            W_response["SentimentScore"]["Positive"])) / Weighted_Denominator
            score_Negative = (score_Negative * 4500 + lenghth_of_last_textwrap * (
            W_response["SentimentScore"]["Negative"])) / Weighted_Denominator
            score_Neutral = (score_Neutral * 4500 + lenghth_of_last_textwrap * (
            W_response["SentimentScore"]["Neutral"])) / Weighted_Denominator
            score_Mixed = (score_Mixed * 4500 + lenghth_of_last_textwrap * (
            W_response["SentimentScore"]["Mixed"])) / Weighted_Denominator

            print('Sentiment scores are:')
            print('Positive Sentiment Score: ', score_Positive)
            print('Negative Sentiment Score: ', score_Negative)
            print('Neutral Sentiment Score: ', score_Neutral)
            print('Mixed Sentiment Score: ', score_Mixed)
            print(news_link_list[indx])
            print(news_headline_list[indx])
            sentiment = response["Sentiment"]
            # print(response["SentimentScore"]["Positive"])

        else:
            if No_of_text_split == 0:
                print("No text found to analyze")

        score_Positive = round(((score_Positive) * 100), 2)
        score_Negative = round(((score_Negative) * 100), 2)
        score_Neutral = round(((score_Neutral) * 100), 2)
        score_Mixed = round(((score_Mixed) * 100), 2)

        sentiment_list.append(sentiment)
        positive_sentiment_score_list.append(str(score_Positive))
        negative_sentiment_score_list.append(str(score_Negative))
        neutral_sentiment_score_list.append(str(score_Neutral))
        mixed_sentiment_score_list.append(str(score_Mixed))

    return neutral_sentiment_score_list, positive_sentiment_score_list, negative_sentiment_score_list


# -----------------------------------------------------------------------------------
# ----------------------------xxxxxxxxxxxxxxxx---------------------------------------
# -----------------------------------------------------------------------------------
# print the output to a pdf
# generates a pdf of our results and returns nothing
def create_pdf(Company, news_headline_list, news_link_list, neutral_sentiment_score_list, positive_sentiment_score_list,
               negative_sentiment_score_list):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 15)

    pdf.cell(ln=1, h=5.0, align='L', w=0, txt=Company.upper(), border=0)
    pdf.ln(5)
    # pdf.set_text_color(0,0,225)
    # pdf.set_font('Arial', '', 11)
    for i in range(len(news_headline_list)):

        pdf.set_font('Arial', 'B', 12)
        pdf.ln(0)
        pdf.cell(10)
        # check for "'latin-1' codec can't encode character" error. Convert to right encoding. *To-do*
        try:
            pdf.multi_cell(h=5.0, align='L', w=0, txt='Headline: ' + news_headline_list[i], border=0)
        except:
            print('Possible presence of invalid latin-1 character')
        print(news_headline_list[i])

        pdf.set_font('Arial', '', 11)
        pdf.ln(0)
        pdf.cell(10)
        pdf.multi_cell(h=5.0, align='L', w=0, txt='Source url: ' + news_link_list[i], border=0)
        print(news_link_list[i])
        '''
        pdf.ln(0)
        pdf.cell(10)
        pdf.multi_cell(h=5.0, align='L', w=0, txt='Sentiment: '+ sentiment_list[i], border=0)
        print(sentiment_list[i])'''

        pdf.ln(0)
        pdf.cell(10)
        pdf.multi_cell(h=5.0, align='L', w=0, txt='Neutral Sentiment Score(%): ' + neutral_sentiment_score_list[i],
                       border=0)
        print(neutral_sentiment_score_list[i])

        pdf.ln(0)
        pdf.cell(10)
        pdf.multi_cell(h=5.0, align='L', w=0, txt='Positive Sentiment Score(%): ' + positive_sentiment_score_list[i],
                       border=0)
        print(positive_sentiment_score_list[i])

        pdf.ln(0)
        pdf.cell(10)
        pdf.multi_cell(h=5.0, align='L', w=0, txt='Negative Sentiment Score(%): ' + negative_sentiment_score_list[i],
                       border=0)
        print(negative_sentiment_score_list[i])

        pdf.ln(0)
        pdf.cell(10)
        pdf.multi_cell(h=0.25, align='L', w=0, txt='', border=1, fill=1)
        pdf.ln(0)

        # pdf.write(5,news_headline_list[1], news_link_list[1])
    pdf.output('Senti_pdf.pdf', 'F')

    return True


# -----------------------------------------------------------------------------------
# -------------------------COMPANY NAME--------------
# -----------------------------------------------------------------------------------


news_detailed_list = []
news_link_list = []
news_headline_list = []

Company = input('Company Name: ')

# call 'webpage_scraping' method to scrape all websites
# returns lists containing detailed news text, and correponding lists of news and summary headlines
news_detailed_list, news_link_list, news_headline_list = webpage_scraping(Company)

# call 'sentiment_score_calculation' method to calculate the sentiment scores using AWS Comprehend
neutral_sentiment_score_list, positive_sentiment_score_list, negative_sentiment_score_list = sentiment_score_calculation(
    news_detailed_list, news_link_list, news_headline_list)

# call 'create_pdf' method to create pdf of our results
# generates pdf and returns nothing
create_pdf(Company, news_headline_list, news_link_list, neutral_sentiment_score_list, positive_sentiment_score_list,
           negative_sentiment_score_list)

# -----------------------------------------------------------------------------------
# ----------------------xxxxxxxxxxxxxxxxxxxxxxxxxx---------------------
# -----------------------------------------------------------------------------------