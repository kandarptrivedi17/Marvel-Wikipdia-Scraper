from bs4 import BeautifulSoup
import requests as r
import pandas as pd
import sys
import time

wikiURL = 'https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe:_Phase_Five#Films' #Phase one URL

#Extract URLs from the movie table
response = r.get(wikiURL)
soup = BeautifulSoup(response.text, 'html.parser')
movietable = soup.find('table', class_='wikitable')

movieurls = []

for row in movietable.find_all('tr'):
    cells = row.find_all('th')

    for cell in cells:
        links = cell.find_all('a', href=True)

    for link in links:
        href = link['href']
        if href.startswith('/wiki/'):
            full_url = f"https://en.wikipedia.org{href}"
            movieurls.append(full_url)

        elif href.startswith('http'):
            movieurls.append(href)


class ThePhaseFive:

    def __init__(self):
        self.intro_para = self.intropara
        self.movies_list = self.movieslist
        self.info_box = self.infobox
        self.movie_plot = self.movieplot
        self.antman_quantumania = self.antmanquantumania
        self.gurdian_ofgalaxy_three = self.gurdianofgalaxythree
        self.the_marvels = self.themarvels
        self.deadpool_wolverine = self.deadpoolwolverine
        self.captainamerica_newworld = self.captainamericanewworld
        self.the_thunderbolts = self.thethunderbolts                

    def writingeffect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()

    #Phase1 Intro Paragraph
    def intropara(self):
        phase5 = r.get(wikiURL)
        soup5 = BeautifulSoup(phase5.content, 'html.parser')
        phase5 = soup5.find_all('p')
        return(self.writingeffect(phase5[1].text))

    #Phase1 Table
    def movieslist(self):
        table = pd.read_html(wikiURL)
        phase5table = (table[2].iloc[:, [0, 1]].copy())
        phase5table.columns = ['Movies Title', 'Release Date']
        phase5table = phase5table.set_index('Movies Title')
        return(phase5table)

    def infobox(self, eachurl):
        response = r.get(eachurl)
        soup = BeautifulSoup(response.content, 'html.parser')
        infobox = soup.find('table', class_='infobox')

        data = {}

        if not infobox:
            print("Infobox not found on this page.")
            exit()

        for row in infobox.find_all('tr'):
            header = row.find('th')
            value = row.find('td')
            if header and value:
                # Clean up text by stripping whitespace and removing reference tags
                key = header.get_text(strip=True)
                val = value.get_text(strip=True)
                data[key] = val

        for key, value in data.items():
            print(f"{key:>25} \t:-:\t {value}")

    def movieplot(self, plotlink):
        response = r.get(plotlink)
        soup = BeautifulSoup(response.content, 'html.parser')
        divheading = soup.find('div', class_='mw-heading')

        if divheading:
            plot_h2 = divheading.find('h2', id='Plot')

            if plot_h2:
                paragraphs = plot_h2.find_all_next(['p', 'h2'])

                for element in paragraphs:
                    if element.name == 'h2':
                        break
                    elif element.name == 'p':
                        print(element.get_text())     

    def antmanquantumania(self):
        self.infobox(movieurls[0])
        print()
        self.movieplot(movieurls[0])

    def gurdianofgalaxythree(self):
        self.infobox(movieurls[1])
        print()
        self.movieplot(movieurls[1])

    def themarvels(self):
        self.infobox(movieurls[2])
        print()
        self.movieplot(movieurls[2])

    def deadpoolwolverine(self):
        self.infobox(movieurls[3])
        print()
        self.movieplot(movieurls[3])

    def captainamericanewworld(self):
        self.infobox(movieurls[4])
        print()
        self.movieplot(movieurls[4])

    def thethunderbolts(self):
        self.infobox(movieurls[5])
        print()
        self.movieplot(movieurls[5])

fifthwiki = ThePhaseFive()
# fifthwiki.intropara()
# print(fifthwiki.movieslist())
# fifthwiki.antmanquantumania()
# fifthwiki.gurdianofgalaxythree()
# fifthwiki.themarvels()
# fifthwiki.deadpoolwolverine()
# fifthwiki.captainamericanewworld()
# fifthwiki.thethunderbolts()
