"""Function(s) that handle printing."""

import streamlit as st


def print_top_articles(found_articles):
    """Print the top articles that appear in found_articles."""
    # print all articles if there are 5 or less
    if len(found_articles) <= 5:
        article_num = 1
        for article in found_articles:
            subheading = "Article " + str(article_num)
            st.subheader(subheading)
            st.write("Title:", article["Title"])
            st.write("Publication Date:", article["Date"])
            # if there 3 or less authors, print all authors
            if len(article["Author(s)"]) <= 3:
                for author in article["Author(s)"]:
                    st.write("Author(s):", author)
            # print first author + " et al."
            else:
                author_string = article["Author(s)"][0] + " et al."
                st.write("Author(s):", author_string)
            article_num += 1
    # print the first 5 articles
    else:
        article_num = 1
        count = 0
        while count <= 4:
            subheading = "Article " + str(article_num)
            st.subheader(subheading)
            st.write("Title:", found_articles[count]["Title"])
            st.write("Publication Date:", found_articles[count]["Date"])
            # if there 3 or less authors, print all authors
            if len(found_articles[count]["Author(s)"]) <= 3:
                for author in found_articles[count]["Author(s)"]:
                    st.write("Author(s):", author)
            # print first author + " et al."
            else:
                author_string = found_articles[count]["Author(s)"][0] + " et al."
                st.write("Author(s):", author_string)
            count += 1
            article_num += 1
