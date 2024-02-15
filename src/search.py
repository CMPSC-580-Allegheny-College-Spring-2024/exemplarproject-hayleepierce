"""Functions that handle searching."""

def find_all(list, string):
    """Return True if all elements occur in the list."""
    for element in list:
        if element not in string:
            return False
    return True

def search_corpus(corpus, search_lists):
    """Return all articles the search lists appear in."""
    found_articles = []
    for search_list in search_lists:
        for article in corpus:
            for paragraph in article['Content']:
                if type(paragraph) != type(None):
                    # search for single words
                    if search_list == search_lists[-1]:
                        if find_all(search_list, paragraph) and article not in found_articles:
                            found_articles.append(article)
                    # search for combinations of words
                    else:
                        for phrase in search_list:
                            if phrase in paragraph and article not in found_articles:
                                found_articles.append(article)
    return found_articles