import streamlit as st
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
from development import develop_search_lists, develop_corpus
from printing import print_top_articles
from search import search_corpus

st.title('Corpus Search')
# location of corpus directory
directory = 'data\corpus'
search = st.text_input('What would you like to search for?')

# develop data structures
search_lists = develop_search_lists(search)
corpus = develop_corpus(directory)

# search through the corpus for search_lists
found_articles = search_corpus(corpus, search_lists)

# if a search was entered print the results
if type(search) != type(None):
    st.write('Number of article found:', len(found_articles))
    percentage = str(int(len(found_articles) / len(corpus) * 100)) + '%'
    st.write('Percentage of total corpus:', percentage)
    # st.write('Positivity percentage:', pos_percentage)
    # st.write('Negativity percentage:', neg_percentage)

    st.header('Top Articles Found', divider='gray')
    print_top_articles(found_articles)
