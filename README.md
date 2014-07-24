ParatextExtractor: code using BeautifulSoup to extract a few variables from PubMed articles
Ver1 - first version (adoy) that only extracts acknowledgements marked with JATS <ack> tag
Ver 2 - extracts a broader range of statements and also counts number of authors per article; also includes one sample bit of text for easy testing

BeautifulSoupReplaceHyphens: simple script that replaces "-" with "_" in all xml variable names (BUT NOT attributes).  This makes it possible to actually parse the files in python, because python does not recognize "-" as a valid variable character.  

preprocessedText.txt: first batch of preprocessed text

ProcessedTextWithAuthorTotals.xlsx: excel spreadsheet containing extracted acknowledgment statements + total number of authors per article, as well as some figures from the paper

sampleData: original files used for testing.
