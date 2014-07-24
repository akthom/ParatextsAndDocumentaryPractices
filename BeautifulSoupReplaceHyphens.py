import re
from bs4 import BeautifulSoup


soup=open("sarcastic-fringehead/sampleData/one.nxml", "lxml")

for i in soup.findAll():
	i.name=i.name.replace("-","_")

n=soup.find_all("article_id", attrs={"pub_id_type": "pmid"})
m=n[0].contents

pmid=str(m[0])

