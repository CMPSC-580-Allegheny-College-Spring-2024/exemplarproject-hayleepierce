"""Function(s) that handle the development of data structures."""

import string
import os
import nltk
from nltk.corpus import stopwords
from itertools import combinations
import xml.etree.ElementTree as ET


def develop_search_lists(search):
    """Develop a list of lists containing strings to search for."""
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    # split the search string
    word_list = search.lower().split()
    # remove stop words
    for word in word_list:
        if word in stop_words:
            word_list.remove(word)
    # remove punctuation
    for index in range(len(word_list)):
        for char in string.punctuation:
            word_list[index] = word_list[index].replace(char, "")
    # create combination of search words
    search_lists = []
    r = list(range(len(word_list)))
    r.reverse()
    for index in r:
        x = combinations(word_list, index + 1)
        combination = [" ".join(i) for i in x]
        search_lists.append(combination)
    return search_lists


def develop_corpus(directory):
    """Develop a list of dictionaries containing the articles' information."""
    corpus = []
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
        title = root.find(".//article-title")
        subtitle = root.find(".//subtitle")
        if type(title) and type(subtitle) != type(None):
            article["Title"] = title.text + ": " + subtitle.text
        elif type(title) != type(None):
            article["Title"] = title.text
        else:
            article["Title"] = "None"
        # find the publication date of the article
        month = root.find(".//month")
        day = root.find(".//day")
        year = root.find(".//year")
        if type(day) != type(None):
            article["Date"] = month.text + "/" + day.text + "/" + year.text
        else:
            article["Date"] = month.text + "/" + year.text
        # find the authors of the article
        authors = []
        surname = root.findall(".//surname")
        given_names = root.findall(".//given-names")
        for name in surname:
            authors.append(name.text)
        count = 0
        for name in given_names:
            if type(name.text) != type(None):
                authors[count] = authors[count] + ", " + name.text
            count += 1
        article["Author(s)"] = authors
        # find all paragraphs within the article
        paragraphs = []
        for paragraph in root.findall(".//p"):
            if type(paragraph.text) != type(None):
                paragraphs.append(paragraph.text.lower())
        article["Content"] = paragraphs
        # add article to corpus
        corpus.append(article)
    return corpus
