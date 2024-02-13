import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import xml.etree.ElementTree as ET
import os
import string
import itertools

# sia = SentimentIntensityAnalyzer()

# st.text_input

search = 'do mammalian cells mutate frequently?'

"""
develop_search_list() function
"""
# develop list of strings to search for
search_list = search.split()
for word in search_list:
    if len(word) < 4:
        search_list.remove(word)
for index in range(len(search_list)):
    for char in string.punctuation:
        search_list[index] = search_list[index].replace(char, '')
complete_search_lists = []
r = list(range(len(search_list)))
r.reverse()
for index in r:
    x = itertools.combinations(search_list, index+1)
    combination = [' '.join(i) for i in x]
    complete_search_lists.append(combination)

"""
develop_corpus() function
"""
corpus = []
directory = 'data\corpus'
# iterate through all xml files in the corpus
for filename in os.listdir(directory):
    # create empty dictionary for new article
    article = {}
    # create the full path for the current file
    path = os.path.join(directory, filename)
    # create element tree for the current file
    tree = ET.parse(path)
    # find root of the element tree
    root = tree.getroot()
    # Find the title of the article
    title = root.find('.//article-title')
    subtitle = root.find('.//subtitle')
    if type(title) and type(subtitle) != type(None):
        article['Title:'] = (title.text + ": " + subtitle.text)
    elif type(title) != type(None):
        article['Title:'] = title.text
    else:
        article['Title:'] = 'None'
    # find the publication date of the article
    month = root.find('.//month')
    day = root.find('.//day')
    year = root.find('.//year')
    if type(day) != type(None):
        article['Date:'] = month.text + '/' + day.text + '/' + year.text
    else:
        article['Date:'] = month.text + '/' +  year.text
    # find the authors of the article
    authors = []
    surname = root.findall('.//surname')
    given_names = root.findall('.//given-names')
    for name in surname:
        if type(name.text) != type(None):
            authors.append(name.text)
    count = 0
    for name in given_names:
        if type(name.text) != type(None):
            authors[count] = authors[count] + ', ' + name.text
            count += 1
    article['Author(s):'] = authors
    # find all paragraphs within the article
    paragraphs = []
    for paragraph in root.findall('.//p'):
        paragraphs.append(paragraph.text)
    article['Content:'] = paragraphs
    # add article to corpus
    corpus.append(article)
    #             for l in complete_search_lists:
    #                 for phrase in l:
    #                     count = 0
    #                     if count < 5:
    #                         if phrase in paragraph:
    # reverse the string to find the begining of the sentence
    #                             #print(phrase)
    #                             #print(paragraph[paragraph.index(phrase)-50
    #                             #                :paragraph.index(phrase)+50])
    #                             count += 1
                