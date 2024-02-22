[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)
# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

This repository contains student project materials, including project report, data, code, and references to literature for this departmentally-sponsored project. __As you complete each of the below sections in this document, please be sure to remove the preamble text so that it does not appear in your work.__ Please work with your first reader to answer any questions or concerns that you may have.

## GitHub Handle: hayleepierce

## Name: Haylee Pierce

## Major: Computer Science (from the former Academic Bulletin)

## Project Name: Corpus Comb

Here, think of an interesting name of the work that bring a freshness and excitement to the area of this project. Consider using a name that carries some information about what the project and provides some hint at what the project does without being too wordy.

---

## Overview

This project consists of a dashboard where a user can search through a corpus of articles for a word/phrase. The number of articles the word/phrase was found in is provided, as well as the percentage of the total corpus that references the word/phrase. The information for the top articles is displayed to the user.

This project assists the user in determining the validity of the word/phrase they search. The user can assume that if a large percentage of the corpus mentions their word/phrase, their word/phrase is likely to be valid.

```
TODO (250 words minimum): Discuss the overview of the project using and building on the project description provided by the department. In this section, a concise summary is discussed of the study's key elements, offering the reader a quick understanding of the research's scope and goals. The section continues to outline the main topics, research questions, hypotheses, and /or theories in a clear and meaningful language to provide a type of roadmap for the reader to navigate the forthcoming details of the project. This section also needs to motivate the project by providing context for the study, outlining the current state of knowledge in the field, and highlighting any gaps or limitations in existing research. The section serves as a foundational guide that enables the reader to grasp the context of the study, in addition to its structure, before moving into a more technically-based discussion in the following sections of the article. In short, the "Overview" section needs to answer the `what` and `why` questions, that is `what is the project?` and `why is the project important?`
```

## Literature Review



```
TODO: Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further contributes to the `why is the project important?` question. The number of scholarly work included in the literature review may vary depending on the project.
```

## Methods

This project uses [Streamlit](https://streamlit.io/) to create a dashboard for the user to input a search and view the corresponding output. A collection of academic articles in the form of XML files from [PubMed](https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/) to develop a corpus. [The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html) is used to parse through the XML files; collecting the following information using the associated tags:

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

The user's input is taken in as a string, the `lower()` function is used to make all characters in the string lowercase, and the `split()` method is used to divide the string into a list. A list of English stopwords from [NLTK](https://www.nltk.org/) is used to remove stopwords from this list. The [`combinations()`](https://docs.python.org/3/library/itertools.html#itertools.combinations) function from the `itertools` module is used to create several sublists of all the different combinations of the remaining words. The sublists are ordered from the sublist containing the combinations using the most words to the sublist containing the singular words.

Iterating through the sublists, the corpus is searched using the "Content" key for each article dictionary. If a string from the sublist is found in the content of an article, the article's dictionary is added to the `found_articles` list (unless it has already been added during a previous search). The final sublist (containing the singular words) is slightly different, with all words having to be found in the article's content for it to be added to `found_articles`.

The number of articles found (the length of `found_articles`) and the percentage of the total corpus the search was found in (the length of `found_articles` divided by the length of the corpus list) is displayed to the user. The top five articles and their information is displayed to the user, as well.

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
5. Type in your desired search in the search bar

```
TODO: The result of your work will be the delivery of some type of artifact which will likely contain software programming solutions (i.e., Python code, HTML pages, or similar). To allow the user to experience and execute your artifact, you must first explain how to set up the initial conditions to run or use the artifact. Be sure to offer explicit details and instructions regarding the installation of the necessary foundational libraries, drivers, external software projects, containers and similar types of tertiary software which are involved in executing your artifact. Once these initial software installations have been completed, then you are asked to offer the necessary instructions for actually executing the artifact. For this, please provide all command line parameters or associated bash commands for execution. Please remember that users are unwilling to "figure-out" how to use code in absence of the essential instructions concerning the execution of project artifacts.
```

## Results and Outcomes

The search "mutated cells" gives the following output:

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

```
TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact
```

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)