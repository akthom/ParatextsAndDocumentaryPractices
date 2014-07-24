#A. Thomer - modding from spring 2013 text mining code for use in paratext project

#python 2.7.2 or NLTK won't work

tester = "BMC_Bioinformatics_2010_Apr_29_11_220.nxml"

def ack1():

        from bs4 import BeautifulSoup
        import re
        import os
        import nltk.data
        import csv


        outfile = open("testingForBMC.csv","a")#, encoding="latin-1") <-- commented out because code was originally written for python 3.2 but then discovered that it broke 2.7

        w=csv.writer(outfile)
        w.writerow(["filename ","PMID ", "AcknowledgementsText"])


        for dirname, dirnames, filenames in os.walk('./sampleData/BMC'): #also modded from something on stack overflow that I now can't find
                
                
                for filename in filenames:
                        if filename.endswith('.nxml'):
                                infile=os.path.join(dirname, filename)

                                
                                soup = BeautifulSoup(open(infile), "lxml") #not sure if xml parsing is actually necessary/helpful
                                for i in soup.findAll():
                                        i.name=i.name.replace("-","_") #replaces hyphens with underscores, which makes some of the processing easier
                                pmidline= soup.findAll("article_id", attrs={"pub-id-type": "pmid"})

                        
                                if not pmidline:   # "Using the implicit booleanness of the empty list is quite pythonic." http://stackoverflow.com/questions/53513/python-what-is-the-best-way-to-check-if-a-list-is-empty
                                        pmid=["None"]
                                else:
                                        pmid=pmidline[0].contents


                                ack=soup.ack
#                                if not ack:
#                                        ack=soup.back.sec.title.parent

#                                if not ack:
#                                        ack1=["none"]
#                                else:
#                                        ack1=soup.back.title.parent.contents
                                #elif not ack:
#                                        ack=["None"]
#                                abstract=soup.abstract
                                
                                print(infile, str(pmid[0]))
                                w.writerow([filename, pmid[0], ack])
        print("done")
        outfile.close()


