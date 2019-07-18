#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:59:34 2019

@author: camillelamy
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:57:57 2019

@author: Cam
"""

from elsapy.elsclient import ElsClient
from elsapy.elsdoc import FullDoc
import json
import re
import 
    
## Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

## Initialize client
client = ElsClient(config['apikey'])


## ScienceDirect (full-text) document example using PII

with open("list_pii_RTM.json") as json_file:  
    pii_code = json.load(json_file)
print ("Liste des codes PII :",pii_code)
print (type(pii_code))




List_PII = re.sub("[^\w]", " ",  pii_code).split()
print ("List_PII",List_PII)
print ("List_PII type",type(List_PII)) 

for i in List_PII:
    
    pii_doc = FullDoc(sd_pii = i)
    print (pii_doc.read(client))
    print(pii_doc.title)
    if pii_doc.read(client):
        #print ("\n\n","Title : \n\n ", pii_doc.title,"\n\n")
        pii_doc.write()   
    else:
        print ("Read document failed.")
    
    
    
    
    """
    

    
    #for i in pii_doc.data["coredata"]["dcterms:subject"][i]["$"]:
        
#    for i in (pii_doc.data["coredata"]["dcterms:subject"][]["$"]):
    #for i in pii_doc.data["coredata"]["dcterms:subject"]:
       # for j in i:
       #     keyword = j[0]["$"]
       #     print(keyword)
        
        #keywords = (pii_doc.data["coredata"]["dcterms:subject"][i]["$"])
        #print (Keywords)
        


    Abstract = pii_doc.data["coredata"]["dc:description"]
    Revue = pii_doc.data["coredata"]["prism:publicationName"]
    Text = pii_doc.data["originalText"]
    
    #print (pii_doc.title,Abstract, Revue)
    Article = str(Revue)+str(pii_doc.title) + str(Abstract)+ str(Text)
    print (Article)
    
    with open("/Users/camillelamy/Dossier_Python/ASS_Project/ASS_Project/article_scrap/data/"+str(re.sub(" ","_",pii_doc.title))+".txt",'w') as outfile:  
        json.dump(Article, outfile)
    

    Abtract, keyword, Revue, Author and texte variable, go to searsh information in data folder. 
    
    
    
#Abstract = pii_doc.data["coredata"]["dc:description"]
Keywords = (pii_doc.data["coredata"]["dcterms:subject"][0]["$"],
            pii_doc.data["coredata"]["dcterms:subject"][1]["$"])
            #pii_doc.data["coredata"]["dcterms:subject"][2]["$"],
            #pii_doc.data["coredata"]["dcterms:subject"][4]["$"],)


Revue = pii_doc.data["coredata"]["prism:publicationName"]
Author = (pii_doc.data["coredata"]["dc:creator"][0]["$"],
          pii_doc.data["coredata"]["dc:creator"][1]["$"],
          pii_doc.data["coredata"]["dc:creator"][2]["$"],)
          
Text = pii_doc.data["originalText"]


print ("Revue: \n\n ",Revue,"\n\n")
print ("Keywords: \n\n ",Keywords,"\n\n")
print ("Author:\n\n",Author,"\n\n")
"""
#itérer pour Keyword et Author