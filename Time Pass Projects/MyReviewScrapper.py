# Review Scrapper 
# input the below 3 inputs correctly and
# see result in Variable Explorer.

#------------------------------
searchString = "boatheadset" # without space

# Enter after 
block_class_name = "_2pi5LC col-12-12"
review_class_name = "t-ZTKy"
#------------------------------

import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

flipkart_url = "https://www.flipkart.com/search?q=" + searchString # preparing the URL to search the product on flipkart
uClient = uReq(flipkart_url) # requesting the webpage from the internet
flipkartPage = uClient.read() # reading the webpage
uClient.close() # closing the connection to the web server
flipkart_html = bs(flipkartPage, "html.parser") # parsing the webpage as HTML
bigboxes = flipkart_html.findAll("div", {"class": block_class_name}) # seacrhing for appropriate tag to redirect to the product link
full_review = []
for i in range(0,500):
    try:
        box = bigboxes[i] #  taking the first iteration (for demo)
        productLink = "https://www.flipkart.com" + box.div.div.div.a['href'] # extracting the actual product link
        prodRes = requests.get(productLink) # getting the product page from server
        prod_html = bs(prodRes.text, "html.parser") # parsing the product page as HTML
        commentboxes = prod_html.find_all('div', {'class': review_class_name}) # finding the HTML section containing the customer comments
        
        reviews = []
        for commentbox in commentboxes:
            try:
                name = commentbox.div.div.text
                reviews.append(name)
            except:
                name = 'No Name'
                reviews.append(name)
        full_review.extend(reviews)
    except:
        continue


#drop duplicates in list
def drop_duplicates_in_list(lst):
    mylst = []
    for i in lst:
        if i in mylst:
            continue
        else:
            mylst.append(i)
    return mylst

result = drop_duplicates_in_list(full_review)


#######################################
# text analysis

from textblob import TextBlob
import pandas as pd
# change to df
df = pd.DataFrame({"Review":result})
lst_of_polarity = []
lst_of_good_and_bad_comments = []
for i in range(df.shape[0]):
    text = df['Review'][i]
    obj = TextBlob(text)
    sentiment = obj.sentiment.polarity
    lst_of_polarity.append(sentiment)
    if sentiment <= 0:
        lst_of_good_and_bad_comments.append("Bad")
    else:
        lst_of_good_and_bad_comments.append("Good")
df["Polarity"] = lst_of_polarity
df["Good_or_Bad_based_on_polarity"] = lst_of_good_and_bad_comments

# print essential parameters

# avg polarity
avg_polarity = df['Polarity'].mean()
print(avg_polarity)
# Good and Bad
Good_and_Bad = df["Good_or_Bad_based_on_polarity"].value_counts()
print(Good_and_Bad)

