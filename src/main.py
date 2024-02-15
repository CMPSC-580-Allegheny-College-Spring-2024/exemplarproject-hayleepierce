import streamlit as st
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
from development import develop_search_lists, develop_corpus
from printing import print_top_articles

# sia = SentimentIntensityAnalyzer()
st.title('Corpus Searcher')
# st.text_input
directory = 'data\corpus'
search = st.text_input('What would you like to search for?')
# search = "do mammalian cells exist?"

search_lists = develop_search_lists(search)
corpus = develop_corpus(directory)

def find_all(list, string):
    for element in list:
        if element not in string:
            return False
    return True

found_articles = []
for search_list in search_lists:
    for article in corpus:
        for paragraph in article['Content']:
            if type(paragraph) != type(None):
                if search_list == search_lists[-1]:
                    if find_all(search_list, paragraph) and article not in found_articles:
                        found_articles.append(article)
                else:
                    for phrase in search_list:
                        if phrase in paragraph and article not in found_articles:
                            found_articles.append(article)

if type(search) != type(None):
    st.write('Number of article found:', len(found_articles))
    percentage = str(int(len(found_articles) / len(corpus) * 100)) + '%'
    st.write('Percentage of total corpus:', percentage)
    # st.write('Positivity percentage:', pos_percentage)
    # st.write('Negativity percentage:', neg_percentage)

    st.header('Top Articles Found', divider='gray')
    print_top_articles(found_articles)
