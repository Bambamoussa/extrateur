
from src.main.PageCheck import *
    
import unittest

class PageCheckTest(unittest.TestCase):
    
    def PageExisteTest(self):
        page=PageCheck("https://fr.wikipedia.org/wiki/Comparateur_de_prix")
        resultat=page.pageExiste()
        self.assertTrue(resultat)

        page1=PageCheck("www.google.com")
        resultat1=page.pageExiste()
        self.assertFalse(resultat1)



    def urlCheckTest(self):
        page=PageCheck("Comparateur_de_prix")
        resultat=page.urlChek()
        b="https://en.wikipedia.org/wiki/Comparateur_de_prix"
        self.assertEqual(resultat,b)
        
 

P=PageCheckTest()
P.urlCheckTest()

