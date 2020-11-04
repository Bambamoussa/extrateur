from PageCheck import *
from Extrator import *
from bs4 import BeautifulSoup
import requests
import os
import codecs
class wikiMatrice:
    def __init__(self):
        self.url=" "

    def interface(self):
        url=input("1-veuillez entrez une url")
        page=PageCheck(url)
        if(page.urlChek()!=" "):
            extract=Extractor(url)
            extract.extraction()
        else:
            print("l'url n\' est pas valide")

    def lister(self):
        f = open("urls.txt", "r")
        for file in f.readline() :
            page=PageCheck(file)
            url=page.urlChekFile()
            
            extract=Extractor(url)
            extract.extraction()
            

# test de la fonction table
if __name__ == "__main__":
    wiki=wikiMatrice()
    #wiki.interface()
    wiki.lister()
    os.system("pause")

        
                          