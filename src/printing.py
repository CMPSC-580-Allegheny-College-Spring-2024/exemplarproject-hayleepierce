import streamlit as st

def print_top_articles(found_articles):
    if len(found_articles) <= 5:
        article_num = 1
        for article in found_articles:
            subheading = "Article " + str(article_num)
            st.subheader(subheading)
            st.write('Title:', article['Title'])
            st.write('Publication Date:', article['Date'])
            if len(article['Author(s)']) <= 3:
                for author in article['Author(s)']:
                    st.write('Author(s):', author)
            else:
                author_string = article['Author(s)'][0] + " et al."
                st.write('Author(s):', author_string)
            article_num += 1
    else:
        article_num = 1
        count = 0
        while count <= 4:
            subheading = "Article " + str(article_num)
            st.subheader(subheading)
            st.write('Title:', found_articles[count]['Title'])
            st.write('Publication Date:', found_articles[count]['Date'])
            if len(found_articles[count]['Author(s)']) <= 3:
                for author in found_articles[count]['Author(s)']:
                    st.write('Author(s):', author)
            else:
                author_string = found_articles[count]['Author(s)'][0] + " et al."
                st.write('Author(s):', author_string)
            count += 1
            article_num += 1