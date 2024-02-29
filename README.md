[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)

# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

## GitHub Handle: hayleepierce

## Name: Haylee Pierce

## Major: Computer Science (from the former Academic Bulletin)

## Project Name:

![Corpus Comb](images/logo.PNG)

_The department's project description can be found [here](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects/tree/main/DataScience)._

---

## 🔎 Overview

**Corpus Comb** is a dashboard created by using [Streamlit](https://streamlit.io/) with which users can search for a word or phrase within a corpus. This corpus is comprised of a collection of academic articles sourced from [PubMed](https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/). These articles are in the form of XML files. The user could add to or replace the existing corpus with their own XML files, but only if the format of these files is consistent with the format of the existing XML files. Future development is planned to improve the process of developing the corpus and increase the number of files the corpus can contain. After the corpus is searched, the number of articles the word or phrase was found within is displayed to the user, as well as the percentage of the total corpus these articles account for. The following information for the top five articles is presented to the user:

- Title
- Publication Date
- Author(s)

**Corpus Comb** was created with to goal of assisting users in determining the validity of the word or phrase they searched. The higher the percentage of the total corpus that references the word or phrase the more likely the word or phrase is to be valid. The information about the articles that is presented to the user can assist them in determining if their word or phrase is valid, as well. The user can use this information to find the articles and do further research about their word or phrase. Future features are planned to improve the tool's ability to assist users.

## 📚 Literature Review

[_Keywords of Search Engine Optimization based on Corpus_](lit/Keywords_of_Search_Engine_Optimization.pdf) studies how keywords affect the likelihood a website is included in the results of a search engine, as well as where the website is ranked in those results (Li, 2021). While **Corpus Comb** does not utilize keywords in relation to the articles, the keywords of the user's input are used to search the corpus. Different combinations of these words are used, and the article discusses how larger combinations of keywords are less beneficial. The usage of machine learning artificial intelligence may be useful in the extraction of keywords from both the user input and the articles. These keywords could be used to perform the search, in place of searching through each paragraph of each article (i.e., saving time and processing power).

[_Research of natural language processing based on dynamic search corpus in cultural translation and emotional analysis_](lit/Research_of_natural_language_processing.pdf) discusses the benefits of using text emotion analysis ("...that is, classify texts according to emotional polarity, which is usually divided into two types: positive and negative emotions") to assist the translation of text (Wang, 2023). The benefits of text emotion analysis pointed out by the author are present within **Corpus Comb**, as well. It is planned to implement [sentiment analysis](#sentiment-analysis) into **Corpus Comb** to help users determine the context with which their search is being discussed. Sentiment analysis is a form of text emotion analysis that determines if the text is positive or negative, returning a ratio of the two values.

## 🧪 Methods

### Developing the Corpus

A collection of academic articles in the form of XML files from [PubMed](https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/) is used to develop a corpus. [The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html) is used to parse through the XML files and collect the following information using the associated tags:

- Title
  - "article-title"
  - "subtitle"
- Date
  - "month"
  - "day"
  - "year"
- Author(s)
  - "surname"
  - "given-names"
- Content
  - "p"

Each article is a dictionary containing all of the above pieces of information as key-value pairs. The **Title** is a concatenated string made up of the "article-title", a colon, and the "subtitle". Some articles do not have an "article-title" and/or "subtitle". In the case of no "subtitle", **Title** consists of just "article-title". If both are missing, the **Title** is set equal to "None". The **Date** is also a concatenated string consisting of the "month", "day", and "year" (a slash between each). Some publication dates only consist of a "month" and "year". The **Author(s)** is a list of concatenated strings made up of the "surname", a comma, and the "given-names". In the case that the author has no "given-names", only the "surname" is added to the list. **Content** is a list of strings, with each string being a paragraph of the article. The `lower()` function is used to make all characters within these strings lowercase. Each of the article dictionaries is added to a list to form the corpus. This process is done using the `develop_corpus()` within [development.py](src/development.py).

### User Input

This project uses [Streamlit](https://streamlit.io/) to create a dashboard for the user to input a search. The user's input is taken in as a string and the `lower()` function is used to make all characters within this string lowercase. Then the `split()` method is used to divide this string into a list. A list of English stopwords sourced from the [NLTK](https://www.nltk.org/) library is used to remove stopwords from this list. The [`combinations()`](https://docs.python.org/3/library/itertools.html#itertools.combinations) function from the `itertools` module is used to create several sublists of all the different combinations the remaining words can create. The sublists are ordered from combinations using the most words to the singular words; therefore, the first articles found will be the ones containing the longest combinations. This process is done using the `develop_search_lists()` within [development.py](src/development.py).

### Searching the Corpus

Iterating through the sublists generated from the user's input, the corpus is searched using the **Content** key for the article dictionaries. If a string from the sublist is found within the content of an article, the article's dictionary is added to the `found_articles` list (unless it has already been added during a previous search). The final sublist (containing the singular words) is slightly different, with all words having to be present within the article for it to be added to `found_articles`. This process is done using the `search_corpus()` within [search.py](src/search.py).

### Output

The results are displayed using the [Streamlit](https://streamlit.io/) dashboard. The number of articles found (the length of `found_articles`) and the percentage of the total corpus the search was found in (the length of `found_articles` divided by the length of the corpus) is displayed to the user. The top five articles (i.e., the first five articles found) and their information are displayed to the user, as well. If less than five articles were found, all articles and their information are displayed. This process is done using the `print_top_articles()` within [printing.py](src/printing.py).

## 👨‍💻 Using the Artifact

To use **Corpus Comb** follow the following steps:

1. Clone the repository
2. Navigate to the repository's directory
3. Install the required dependencies by running the following command:
    - `python -m pip install -r requirements.txt`
4. Start the dashboard by running the following command:
    - `python -m streamlit run src/main.py`
5. Enter your desired search into the search bar

To **add** to the corpus follow the following steps:

1. Ensure your articles are:
    - in the form of XML files
    - contain the required tags for the process of [corpus development](#developing-the-corpus)
2. Add the XML files to the [corpus](data/corpus/) folder
3. Delete the [corpus](data/corpus/) folder

To **replace** the corpus follow the following steps:

1. Ensure your articles are:
    - in the form of XML files
    - contain the required tags for the process of [corpus development](#developing-the-corpus)
2. Delete the contents of the [corpus](data/corpus/) folder
3. Place your XML files in the [corpus](data/corpus/) folder

## 🔬 Testing and Results

This project was tested manually using a series of inputs varying in length, punctuation, and case.

The search "fun guy" found a bug in the previous method of removing stop words, which was designed to remove all words with less than 4 characters. When given the search "fun guy" both words should have been removed, but only the word "fun" was removed. This manner of removing stopwords was grossly inefficient; therefore, it was replaced by the [current method](#user-input).

The project originally did not account for cases. After finding drastically different results for the searches "fish" and "Fish", code was added to change all characters within the user input and article paragraphs to lowercase during the development of the [search lists](#user-input) and [corpus](#developing-the-corpus).

Below are the results produced by three of the different searches used during testing:

Search: "mutated cells"

```markdown
Number of article found: 21

Percentage of total corpus: 1%

Top Articles Found
Article 1
Title: Activation of mammalian Chk1 during DNA replication arrest: a role for Chk1 in the intra-S phase checkpoint monitoring replication origin firing

Publication Date: 9/3/2001

Author(s): Feijoo, Carmen et al.

Article 2
Title: A modified version of a Fos-associated cluster in HBZ affects Jun transcriptional potency

Publication Date: 5/22/2006

Author(s): Hivin, Patrick et al.

Article 3
Title: RMCE-ASAP: a gene targeting method for ES and somatic cells to accelerate phenotype analyses

Publication Date: 7/26/2006

Author(s): Toledo, Franck et al.

Article 4
Title: Transcriptional potential of the γ-globin gene is dependent on the CACCC box in a developmental stage-specific manner

Publication Date: 8/12/2006

Author(s): Li, Qiliang et al.

Article 5
Title: Structural basis of yeast aminoacyl-tRNA synthetase complex formation revealed by crystal structures of two binary sub-complexes

Publication Date: 8/12/2006

Author(s): Simader, Hannes et al.
```

Search: "How do mammalian cells adapt to surroundings?"

```markdown
Number of article found: 89

Percentage of total corpus: 5%

Top Articles Found
Article 1
Title: Activation of mammalian Chk1 during DNA replication arrest: a role for Chk1 in the intra-S phase checkpoint monitoring replication origin firing

Publication Date: 9/3/2001

Author(s): Feijoo, Carmen et al.

Article 2
Title: Spatial distribution and specification of mammalian replication origins during G1 phase

Publication Date: 4/28/2003

Author(s): Li, Feng et al.

Article 3
Title: The DNA polymerase λ is required for the repair of non-compatible DNA double strand breaks by NHEJ in mammalian cells

Publication Date: 5/31/2006

Author(s): Capp, Jean-Pascal et al.

Article 4
Title: Dominant-negative Pes1 mutants inhibit ribosomal RNA processing and cell proliferation via incorporation into the PeBoW-complex

Publication Date: 5/31/2006

Author(s): Grimm, Thomas et al.

Article 5
Title: Dynamic recruitment of transcription factors and epigenetic changes on the ER stress response gene promoters

Publication Date: 6/6/2006

Author(s): Donati, Giacomo et al.
```

Search: "Red Fish"

```markdown
Number of article found: 26

Percentage of total corpus: 1%

Top Articles Found
Article 1
Title: The replication timing program of the Chinese hamster

Publication Date: 7/23/2001

Author(s): Li, Feng et al.

Article 2
Title: Mutagenic nucleotide incorporation and hindered translocation by a food carcinogen C8-dG adduct in

Publication Date: 7/4/2006

Author(s): Zhang, Ling et al.

Article 3
Title: Royal Jelly Prevents Osteoporosis in Rats: Beneficial Effects in Ovariectomy Model and in Bone Tissue Culture Model

Publication Date: 9/24/2006

Author(s): Hidaka, Saburo et al.

Article 4
Title: NATsDB: Natural Antisense Transcripts DataBase

Publication Date: 1/1/2007

Author(s): Zhang, Yong et al.

Article 5
Title: Troubleshooting coupled

Publication Date: 11/11/2006

Author(s): Iskakova, Madina B. et al.
```

## 🛠️ Future Work

### Pickle

[_Pickle_](https://docs.python.org/3/library/pickle.html) is a Python module that allows for the serializing and de-serializing of a Python object structure. The use of this module would allow the corpus to be serialized after it is developed and then de-serialized for reuse. This would remove the need to re-develop the corpus for each of the searches the user inputs; as a result, decreasing the amount of time and processing required for each search. This would also allow the size of the corpus to be significantly increased.

### Sentiment Analysis

Sentiment analysis is the technique of processing text data and developing positivity and negativity scores based on the provided text. The [_SentimentIntensityAnalyzer_](https://www.nltk.org/api/nltk.sentiment.SentimentIntensityAnalyzer.html?highlight=positive+negative) from the NLTK library can be used to implement this technique into **Corpus Comb**. The sentence(s) in which the user's input was found would be used by the _SentimentIntensityAnalyzer_ to develop positivity and negativity scores for each article. These scores would then be used to find the average a positivity and negativity score. These scores would be presented to the user; therefore, giving them an idea of if their search is discussed in a positive or negative light within the articles.

### Test Suite

A series of test cases (a test suite) should be developed to ensure that all the code performs as intended. Due to the strict deadline on this project automated testing using a test suite was unable to be implemented.

## 🔗 References

- Li, R. (2021). Keywords of Search Engine Optimization based on Corpus. _Journal of Physics: Conference Series_.

- Wang, J. (2023). Research of natural language processing based on dynamic search corpus in cultural translation and emotional analysis. _Soft Computing, 27_(11), 7647–7655.
