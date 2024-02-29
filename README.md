[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)

# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

## GitHub Handle: hayleepierce

## Name: Haylee Pierce

## Major: Computer Science (from the former Academic Bulletin)

## Project Name: Corpus Comb

_The department's project description can be found [here](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects/tree/main/DataScience)._

---

## Overview

**Corpus Comb** is a dashboard created by using [Streamlit](https://streamlit.io/) with which users can search for a word or phrase within a corpus. This corpus is comprised of a collection of academic articles sourced from [PubMed](https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/). These articles are in the form of XML files. The user could add to or replace the existing corpus with their own XML files, but only if the format of these files is consistent with the format of the existing XML files. Future development is planned to improve the process of developing the corpus and increase the number of files the corpus can contain. After the corpus is searched, the number of articles the word or phrase was found within is displayed to the user, as well as the percentage of the total corpus these articles account for. The following information for the top five articles is presented to the user:

- Title
- Publication Date
- Author(s)

**Corpus Comb** was created with to goal of assisting users in determining the validity of the word or phrase they searched. The higher the percentage of the total corpus that references the word or phrase the more likely the word or phrase is to be valid. The information about the articles that is presented to the user can assist them in determining if their word or phrase is valid, as well. The user can use this information to find the articles and do further research about their word or phrase. Future features are planned to improve the tool's ability to assist users.

## Literature Review



(Li, 2021) (Wang, 2023)
```
TODO: Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further contributes to the `why is the project important?` question. The number of scholarly work included in the literature review may vary depending on the project.
```

## Methods

### Developing the Corpus

A collection of academic articles in the form of XML files from [PubMed](https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/) is used to develop a corpus. [The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html) is used to parse through the XML files; collecting the following information using the associated tags:

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

Each article is a dictionary with each of the above pieces of information as a key-value pair. The Title is a concatenated string made up of the "article-title", a colon, and the "subtitle". Some articles do not have an "article-title" and/or "subtitle". In the case of no "subtitle", Title consists of just "article-title". If both are missing, the Title is set equal to "None". The Date is also a concatenated string with the "month", "day", and "year" with a `/` between each. Some of the articles' publication date only consists of a "month" and "year". The Author(s) is a list of concatenated strings made up of the "surname, a comma, and the "given-names". In the case that the author only has a "surname", only the "surname" is added to the list. Content is a list of strings, with each string being a paragraph from the article. The `lower()` function is used to make all characters in these strings lowercase. These article dictionaries are added to a list to form the corpus.

### User Input

This project uses [Streamlit](https://streamlit.io/) to create a dashboard for the user to input a search. The user's input is taken in as a string, the `lower()` function is used to make all characters in the string lowercase, and the `split()` method is used to divide the string into a list. A list of English stopwords from [NLTK](https://www.nltk.org/) is used to remove stopwords from this list. The [`combinations()`](https://docs.python.org/3/library/itertools.html#itertools.combinations) function from the `itertools` module is used to create several sublists of all the different combinations of the remaining words. The sublists are ordered from the sublist containing the combinations using the most words to the sublist containing the singular words.

### Searching the Corpus

Iterating through the sublists, the corpus is searched using the "Content" key for each article dictionary. If a string from the sublist is found in the content of an article, the article's dictionary is added to the `found_articles` list (unless it has already been added during a previous search). The final sublist (containing the singular words) is slightly different, with all words having to be found in the article's content for it to be added to `found_articles`.

### Output

The results are displayed using the [Streamlit](https://streamlit.io/) dashboard. The number of articles found (the length of `found_articles`) and the percentage of the total corpus the search was found in (the length of `found_articles` divided by the length of the corpus list) is displayed to the user. The top five articles and their information is displayed to the user, as well.

```
TODO: Discuss the methods of the project to be able to answer the `how` question (`how was this project completed?`). The methods section in an academic research outlines the specific procedures, techniques, and methodologies employed to conduct the study, offering a transparent and replicable framework for the research. It details the resources behind the work, in terms of, for example, the design of the algorithm and the experiment(s), data collection methods, applied software libraries, required tools, the types of statistical analyses and models which are applied to ensure the rigor and validity of the study. This section provides clarity for other researchers to understand and potentially replicate the study, contributing to the overall reliability and credibility of the research findings.
```

## Using the Artifact

To use this Artifact follow the following steps:

1. Clone the repository
2. Navigate to the repository's directory
3. Install the required dependencies by running the following command:
    - `python -m pip install -r requirements.txt`
4. Start the dashboard by running the following command:
    - `python -m streamlit run src/main.py`
5. Enter your desired search into the search bar

```
TODO: The result of your work will be the delivery of some type of artifact which will likely contain software programming solutions (i.e., Python code, HTML pages, or similar). To allow the user to experience and execute your artifact, you must first explain how to set up the initial conditions to run or use the artifact. Be sure to offer explicit details and instructions regarding the installation of the necessary foundational libraries, drivers, external software projects, containers and similar types of tertiary software which are involved in executing your artifact. Once these initial software installations have been completed, then you are asked to offer the necessary instructions for actually executing the artifact. For this, please provide all command line parameters or associated bash commands for execution. Please remember that users are unwilling to "figure-out" how to use code in absence of the essential instructions concerning the execution of project artifacts.
```

## Testing and Results

This project was tested manually using a series of inputs varying in length, punctuation, and case.

The search "fun guy" found a bug in the previous method of removing stop words, which was designed to remove all words with less than 4 characters. When given the search "fun guy" both words should have been removed, only the word "fun" was removed. This manner of removing stopwords was grossly inefficient; therefore, it was replaced by the current method.

The project originally did not account for cases. After finding drastic results for the searches "fish" and "Fish", code was added to change all inputs and paragraphs to lowercase during the development of the search lists and corpus.

Below are the results of three different searches:

Search: "mutated cells"

```
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

```
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

```
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

```
TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact
```

## Future Work

### [Pickle](https://docs.python.org/3/library/pickle.html)

### [Sentiment Analysis](https://www.nltk.org/api/nltk.sentiment.SentimentIntensityAnalyzer.html?highlight=positive+negative)

### Test Suite
