from bs4 import BeautifulSoup
import requests as r
import pandas as pd
import sys
import time

wikiURL = 'https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films' #Phase one URL

#Extract URLs from the movie table
response = r.get(wikiURL)
soup = BeautifulSoup(response.text, 'html.parser')
movietable = soup.find('table', class_='wikitable')

class TheFuture:

    def __init__(self):
        self.intro_para = self.intropara
        self.movies_list = self.movieslist

    def writingeffect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()

    #Phase1 Intro Paragraph
    def intropara(self):
        phasefuture = r.get(wikiURL)
        soupfuture = BeautifulSoup(phasefuture.content, 'html.parser')
        phasefuture = soupfuture.find_all('p')
        return(self.writingeffect(phasefuture[17].text))

    #Phase1 Table
    def movieslist(self):
        table = pd.read_html(wikiURL)
        phase6table = (table[8].iloc[:, [0, 5]].copy())
        phase6table.columns = ['Movies Title', 'Status']
        phase6table = phase6table.set_index('Movies Title')
        return(phase6table)
 
futurefilms = TheFuture()
# futurefilms.intropara()
# print(futurefilms.movieslist())
