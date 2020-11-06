from bs4 import BeautifulSoup
import requests
import os
import codecs
class PageCheck:

    def __init__(self,url):
        self.url=url

    def pageExiste(self):
        existe=False
        response=requests.get(self.url)
        status_code=response.status_code
        if (status_code==200):
            regex=self.url.split(".")
            if "wikipedia" in regex:
                existe=True
                 
        return existe 

    def urlChek(self):
        regex1=self.url.split(":")
        regex=" ".join(regex1)
        if(regex.startswith("https")==False):
            urlp="https://en.wikipedia.org/wiki/"+ self.url
            
        elif(self.pageExiste()):
            urlp=self.url
        else:
            urlp=" "    
        return urlp
     
   