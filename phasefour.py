from bs4 import BeautifulSoup
import requests as r
import pandas as pd
import sys
import time

wikiURL = 'https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe:_Phase_Four#Films' #Phase one URL

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


class ThePhaseFour:

    def __init__(self):
        self.intro_para = self.intropara
        self.movies_list = self.movieslist
        self.info_box = self.infobox
        self.movie_plot = self.movieplot
        self.black_widow = self.blackwidow
        self.shangchi_andtenrings = self.shangchiandtenrings
        self.the_eternals = self.theeternals
        self.spider_nowayhome = self.spidernowayhome
        self.doctorstrange_multiverse = self.doctorstrangemultiverse
        self.thor_lovethunder = self.thorlovethunder
        self.wakanda_forever = self.wakandaforever
        
        

    def writingeffect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()

    #Phase1 Intro Paragraph
    def intropara(self):
        phase4 = r.get(wikiURL)
        soup4 = BeautifulSoup(phase4.content, 'html.parser')
        phase4 = soup4.find_all('p')
        return(self.writingeffect(phase4[1].text))

    #Phase1 Table
    def movieslist(self):
        table = pd.read_html(wikiURL)
        phase4table = (table[2].iloc[:, [0, 1]].copy())
        phase4table.columns = ['Movies Title', 'Release Date']
        phase4table = phase4table.set_index('Movies Title')
        return(phase4table)

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

    def blackwidow(self):
        self.infobox(movieurls[0])
        print()
        self.movieplot(movieurls[0])

    def shangchiandtenrings(self):
        self.infobox(movieurls[1])
        print()
        self.movieplot(movieurls[1])

    def theeternals(self):
        self.infobox(movieurls[2])
        print()
        self.movieplot(movieurls[2])

    def spidernowayhome(self):
        self.infobox(movieurls[3])
        print()
        self.movieplot(movieurls[3])

    def doctorstrangemultiverse(self):
        self.infobox(movieurls[4])
        print()
        self.movieplot(movieurls[4])

    def thorlovethunder(self):
        self.infobox(movieurls[5])
        print()
        self.movieplot(movieurls[5])

    def wakandaforever(self):
        self.infobox(movieurls[6])
        print()
        self.movieplot(movieurls[6])

fourthwiki = ThePhaseFour()
# fourthwiki.intropara()
# print(fourthwiki.movieslist())
# fourthwiki.blackwidow()
# fourthwiki.shangchiandtenrings()
# fourthwiki.theeternals()
# fourthwiki.spidernowayhome()
# fourthwiki.doctorstrangemultiverse()
# fourthwiki.thorlovethunder()
# fourthwiki.wakandaforever()
