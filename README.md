this directory contains code and files from <br>
Weber, N. & Thomer, A. (2014). Paratexts and Documentary Practices: Text Mining Authorship and Acknowledgement from a Bioinformatics Corpus.  In Examining Paratextual Theory and its Applications in Digital Culture. Nadine Desrochers and Daniel Apollon, eds. IGI Global Press. Hershey, Pennsylvania. <br>
and <br>
Thomer, A., Weber, N. (2014). Using Named Entity Recognition as a Classification Heuristic.  Poster presented at iConference 2014.  Berlin. http://hdl.handle.net/2142/47362 <br>
and<br>
Weber, N., Thomer, A. (2014). Automating the Classification of Author Contribution Statements.  Poster presented at the International Digital Curation Conference.  San Francisco, CA.
<p>
email us at thomer2@illinois.edu with any questions -- some of these files might be messy.

ParatextExtractor: code using BeautifulSoup to extract a few variables from PubMed articles
Ver1 - first version (adoy) that only extracts acknowledgements marked with JATS <ack> tag
Ver 2 - extracts a broader range of statements and also counts number of authors per article; also includes one sample bit of text for easy testing

BeautifulSoupReplaceHyphens: simple script that replaces "-" with "_" in all xml variable names (BUT NOT attributes).  This makes it possible to actually parse the files in python, because python does not recognize "-" as a valid variable character.  

preprocessedText.txt: first batch of preprocessed text

ProcessedTextWithAuthorTotals.xlsx: excel spreadsheet containing extracted acknowledgment statements + total number of authors per article, as well as some figures from the paper

ListOfAcknowledgedPersons.xlsx: spreadsheet containing PMIDS, Acknoweldged Persons, and Number of Acknowledged persons
SampleData: original files used for testing.
