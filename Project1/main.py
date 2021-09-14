import json
import requests
import nltk
import streamlit as st
import numpy as np
import pandas as pd

from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

import main_functions
from pprint import pprint

from wordcloud import WordCloud
import matplotlib.pyplot as plt
#nltk.download("punkt")
#nltk.download("stopwords")

api_key_dict = main_functions.read_from_file("JSON_files/api_key.json")
api_key = api_key_dict["my_key"]

st.title("I - Part A - The Top Stories API ")

name = st.text_input("Please enter your name ")

selection = st.selectbox(
    "Please select one of the options",
    ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine", "movies", "nyregion",
     "obituaries", "opinion", "politics", "realestate", "science", "sports", "sundayreview", "technology", "theater", "t-magazine", "travel", "upshot", "us", "world"]
)

st.write("Welcome " + name + "your choice is " + selection)
choice = str(selection)

st.title("II - Part B - Most Popular")

time = st.selectbox(
    "Select the amount of time you want to collect articles from",
    ["1 day", "7 days", "30 days"]
)

st.write("Selected amount of time is " + time)

days = str(time)

if days == "1 day":
    url1 = "https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key=" + api_key
elif days == "7 days":
    url1 = "https://api.nytimes.com/svc/mostpopular/v2/shared/1/facebook.json?api-key=" + api_key
elif days == "30 days":
    url1 = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=" + api_key










url = "https://api.nytimes.com/svc/topstories/v2/"+ choice +".json?api-key=" + api_key

if st.checkbox("Click here to generate specified day feeds"):
     response = requests.get(url1).json()
else:
     response = requests.get(url).json()


main_functions.save_to_file(response,"JSON_files/response.json")
my_articles = main_functions.read_from_file("JSON_files/response.json")

print(type(my_articles))

pprint(my_articles)

str1 = ""
for i in my_articles["results"]:
    str1 = str1 + i["abstract"]
print(str1)

sentences = sent_tokenize(str1)

print(len(sentences))

print(sentences)

words = word_tokenize(str1)

# print(len(words))
#
# print(words)

fdist = FreqDist(words)

# print(fdist.most_common(10))

words_no_punc = []

for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())
# pprint(words_no_punc)

fdist2 = FreqDist(words_no_punc)

pprint(fdist2.most_common(10))

stopwords = stopwords.words("english")

print(stopwords)

clean_words = []

for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)

print(len(clean_words))

fdist3 = FreqDist(clean_words)

pprint(fdist3.most_common(10))

wordcloud = WordCloud().generate(str1)

plt.figure(figsize=(12,12))
plt.imshow(wordcloud)

plt.axis("off")
plt.show()

st.subheader("III - Wordcloud")
if st.checkbox("Click here to generate wordcloud"):
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()







