from bs4 import BeautifulSoup
import requests as r
import pandas as pd
import sys
import time

wikiURL = 'https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe:_Phase_Six#Films' #Phase one URL

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


class ThePhaseSix:

    def __init__(self):
        self.intro_para = self.intropara
        self.movies_list = self.movieslist
        self.info_box = self.infobox
        self.movie_plot = self.movieplot
        self.the_fantasticfour = self.thefantasticfour
        self.spider_brandnewday = self.spiderbrandnewday
        self.avengers_doomsday = self.avengersdoomsday
        self.avengers_secretwars = self.avengerssecretwars                

    def writingeffect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()

    #Phase1 Intro Paragraph
    def intropara(self):
        phase6 = r.get(wikiURL)
        soup6 = BeautifulSoup(phase6.content, 'html.parser')
        phase6 = soup6.find_all('p')
        return(self.writingeffect(phase6[1].text))

    #Phase1 Table
    def movieslist(self):
        table = pd.read_html(wikiURL)
        phase6table = (table[2].iloc[:, [0, 1]].copy())
        phase6table.columns = ['Movies Title', 'Release Date']
        phase6table = phase6table.set_index('Movies Title')
        return(phase6table)

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

    def thefantasticfour(self):
        self.infobox(movieurls[0])
        print()
        print("Plot: On a 1960s-inspired retro-futuristic parallel Earth,[1][2] the Fantastic Four must protect their world from the planet-devouring cosmic being Galactus and his herald, the Silver Surfer.[1]")

    def spiderbrandnewday(self):
        self.infobox(movieurls[1])
        print()
        self.movieplot(movieurls[1])

    def avengersdoomsday(self):
        self.infobox(movieurls[2])
        print()
        print("Plot: Fourteen months after the events of Thunderbolts* (2025), the Avengers, Wakandans, Fantastic Four, New Avengers, and the original X-Men team up to face Doctor Doom.[1][2]")

    def avengerssecretwars(self):
        self.infobox(movieurls[3])
        print()
        print("Secret Wars is scheduled for release on December 17, 2027, both part of Phase Six of the MCU.")

 
sixthwiki = ThePhaseSix()
# sixthwiki.intropara()
# print(sixthwiki.movieslist())
# sixthwiki.thefantasticfour()
# sixthwiki.spiderbrandnewday()
# sixthwiki.avengersdoomsday()
# sixthwiki.avengerssecretwars()
