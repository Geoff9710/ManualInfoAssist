# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:45:03 2018

@author: AkSangwan
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:30:47 2018

@author: AkSangwan
"""

# -*- coding: utf-8 -*-


# import feedparser
from bs4 import BeautifulSoup
from urllib.request import urlopen
# import json
# import ssl
# import boto3
import re


# import nltk


# method for constructionenquirer.com text scraping
def construction_enquirer(Company):
    Punc_removed_text = ''
    html = None
    news_link = []
    news_summary = []

    try:
        html = urlopen('http://www.constructionenquirer.com/').read()
    except:
        print('#1 Const Enquirer url open fail')

    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
    # texts = soup.find_all(text=True)

    # get all the relevant headings and paragraph content from their html tags
    if soup is not None:
        try:
            h3_field = soup.find('div', class_='site-content').find_all('h3')
        except:
            print("#2 Const Enquirer h3_fiels error")
        try:
            p_field = soup.find('div', class_='site-content').find_all('p')
        except:
            print("#3 Const Enquirer p_field error")

    headings = []
    paragraphs = []
    url = []

    # get the headings and the url link
    for x in h3_field:
        headings.append(str(x))
        y = (x.findAll('a', attrs={'href': re.compile("^http://")}))
        if (len(y)) > 0:
            link = y[0].get('href')
            url.append(str(link))

    # get the paragraphgs content
    for x in p_field:
        paragraphs.append(str(x))

    # removing urls and other punctuations within <> tags
    for ind in range(len(headings)):
        Head = headings[ind]
        headings[ind] = re.sub('<[^>]+>', '', Head)

    # removing urls and other punctuations within <> tags
    for ind in range(len(paragraphs)):
        Body = paragraphs[ind]
        paragraphs[ind] = re.sub('<[^>]+>', '', Body)

    # Get the text out of the heading urls which contains this company name

    News_list = []

    CompanyName = Company.lower()

    if (len(headings) > 0 and len(url) > 0):
        for indx in range(len(headings)):
            if (CompanyName in headings[indx].lower()):  # or CompanyName in paragraphs[indx]):
                news_html = None
                try:
                    news_html = urlopen(url[indx]).read()

                except:
                    print('loop url open fail')

                if news_html is not None:
                    news_html_soup = BeautifulSoup(news_html, 'html.parser')
                    try:
                        news_text = news_html_soup.find('div', class_='entry-content').find_all('p')
                    except:
                        print("#4 Const Enquirer error of news_text collection")

                    # find content from url and save all the relevant text, urls and headings for further sentiment analysis
                    if ("" != news_text):
                        news_text = re.sub('<[^>]+>', '', str(news_text))
                        Punc_removed_text = re.sub(r'[^\w\s]', '', str(news_text))
                        News_list.append(Punc_removed_text)
                        news_link.append(url[indx])
                        news_summary.append(headings[indx])
                        # print((Punc_removed_text))

    return News_list, news_link, news_summary


'''
try:
    html = urlopen('http://www.constructionenquirer.com/').read()
    except:
    print('url open fail')   
#call the method to get all relevant text from the website   
x = (construction_enquirer(html))'''

'''def motor_transport(html):
    soup = BeautifulSoup(html, 'html.parser')
    h3_field = soup.find('div', class_='mh-excerpt').find_all('p')
    print(h3_field)
    return True'''

'''def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    elif re.match(r"[\s\r\n]+",str(element)):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.find_all(text=True)
    h3_field = soup.find('div', class_='site-content').find_all('h3')
    p_field = soup.find('div', class_='site-content').find_all('p')
    print(h3_field[7])
    print(p_field[7])

    #visible_texts = filter(tag_visible, texts)     
    #print(visible_texts)
    #print(texts)
    return True#u" ".join(t.strip() for t in visible_texts)
'''

# y = (motor_transport(html))
# x = re.sub(r'[^\w\s]','',x)
# print(x)
# print(type(x))


# y = x.replace( '\n', ' '    )
# with open('trial.txt', 'w') as outfile:
#    json.dump(y, outfile)

# date_field = soup.find('div', class_='post-template-default single single-post postid-201860 single-format-standard')#.find('dt', text='Date')
# print(date_field)
# print date_field.find_next_sibling('dd').text.strip()

'''

url = "https://www.bbc.co.uk/news/business"
html = urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text.encode('utf-8'))
'''

# print(len(content.find_all('p')))
# print(content.prettify())
# questions = content.select('.question-summary')

'''
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote_page)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
print(soup)
'''

'''    
# List with google queries I want to make
desired_google_queries = ['World Fuel Services' , 'Fortune 91', 'Miami', 'Data Science', 'AI', 'ML']

for query in desired_google_queries:
    url = 'http://google.com/search?q=' + query
    # For avoiding 403-error using User-Agent
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    response = urllib.request.urlopen( req )
    html = response.read()
    # Parsing response
    soup = BeautifulSoup(html, 'html.parser')
    # Extracting number of results
    resultStats = soup.find(id="resultStats").string
    print(resultStats)
'''

'''raw_html = open('https://motortransport.co.uk').read()
print(raw_html)'''
'''
def simple_get(url):
   try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
   except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

'''

# store all description content in the rss feed in variable 'tt'
'''
tt=''
for indx in range(len(content)):
    url = content[indx]
    parsedFeed = feedparser.parse(url)
    for feed in parsedFeed.entries: # add titles also to the list
       tt = tt + feed.description + ';'

#lower the entire text to maintain uniformity
lower_text = tt.lower() 

#lower_text = re.sub(r'^https?:\/\/.*[\r\n]*', '', lower_text, flags=re.MULTILINE)
lower_text = re.sub(r'<.+?>', '', lower_text)
#print(lower_text)

#split the text with ';' to save each line in a list
line_split = lower_text.split(';')
#print(t)
#print(content[0])
#for index in range(len(content))    

#lower_text = text.lower() 
#line_split = lower_text.split(';')



# enter the phrase to search in the text

with open("100CompanyList.txt") as company_name:
    Comp_Name = company_name.readlines()
Comp_Name = [x.strip() for x in Comp_Name]

NewList = []

for ind in range(len(Comp_Name)): 
   Comp_Name_L = Comp_Name[ind].lower()
   for index in range(len(line_split)):
      if Comp_Name_L in line_split[index] and len(Comp_Name_L) > 0:#checking if it is not blank space in company list
         NewList.append(line_split[index])
      #else:
         #print('No') 
#print(len(NewList))

final_text = ''
for i in range(len(NewList)):
    final_text = final_text+NewList[i]+' '


Punc_removed_text = re.sub(r'[^\w\s]','',final_text)

#print(Punc_removed_text)
#print('\n')
#x = nltk.download('stopwords')
#sw = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#filtered_words = [word for word in Punc_removed_text if word not in sw]

#print(filtered_words)


#search for the Company name/ phrase in each line of the text and save the line if the text appears

#JoinedList = ('.'.join(NewList))

df = pd.DataFrame({'NewsFeed':NewList})
#print(df)
#d = json.dumps(JoinedList)

#append each lines from dataframe to a list to output a json
temp=[]
for row in df.iterrows():
    index, data = row
    temp.append(data.tolist())

#output a json file
with open('data.json', 'w') as outfile:
    json.dump(temp, outfile)

'''

# client = boto3.client('sts', verify=False, aws_session_token= 837524)
# response = client.get_caller_identity()
# print(response)
# response = client.detect_sentiment(Text=lower_text,LanguageCode='en')
# print(response["Sentiment"])

# uni_str = lower_text.decode('utf-8','ignore')
# print(uni_str)

'''
Str = "Get the output"
u = unicode(Str, "utf-8")  
print(u)

city = 'Ribeir\xc3\xa3o Preto'
print (city.decode('cp1252').encode('utf-8'))


'''

'''
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

'''