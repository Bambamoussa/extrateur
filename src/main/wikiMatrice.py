from PageCheck import *
from Extrator import *
from bs4 import BeautifulSoup
import requests
import os
import codecs
class wikiMatrice:
    def __init__(self):
        self.url=" "

    def saisirUrl(self):
        url=input("veuillez entrez une url ")
        page=PageCheck(url)
        if(page.urlChek()!=" "):
            extract=Extractor(url)
            extract.extraction()
            print("le nombre de tableau est {} ".format(extract.countTable(url)))
        else:
            print("l'url n\' est pas valide")

    def lister(self):
        f = open("urls.txt", "r")
        fichier_entier = f.read()
        files = fichier_entier.split("\n")
        for file in files :
            page=PageCheck(file)
            url=page.urlChek()
            if(url!=" "):
                extract=Extractor(url)
                extract.extraction()
                print("le nombre de tableau est {} ".format(extract.countTable(url)))
            else:
                print("l'url n\' est pas valide") 
            
    def interface(self):
        url=input("saisir 1 pour  ajouter une url \n saisir 2 pour lister pour récuperer les tableaux des urls du fichier ")
        if(url=='1'):
            self.saisirUrl()
        elif(url=='2'):
            self.lister()
        else:
            print(" veuillez saisir un nombre correcte ")
# test de la fonction table
if __name__ == "__main__":
    wiki=wikiMatrice()
    #wiki.interface()
    #wiki.lister()
    wiki.interface()
    

        
                          