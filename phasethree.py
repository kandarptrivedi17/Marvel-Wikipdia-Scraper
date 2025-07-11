from bs4 import BeautifulSoup
import requests as r
import pandas as pd
import sys
import time

wikiURL = 'https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe:_Phase_Three' #Phase one URL

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


class ThePhaseThree:

    def __init__(self):
        self.intro_para = self.intropara
        self.movies_list = self.movieslist
        self.info_box = self.infobox
        self.movie_plot = self.movieplot
        self.civil_war = self.civilwar
        self.doctor_strange = self.doctorstrange
        self.gaurdian_galaxy_two = self.gaurdiangalaxytwo
        self.spider_home_coming = self.spiderhomecoming
        self.thor_ragnarok = self.thorragnarok
        self.black_panther = self.blackpanther
        self.infinity_war = self.infinitywar
        self.antman_wasp = self.antmanwasp
        self.captain_marvel = self.captainmarvel
        self.end_game = self.endgame
        self.spider_far_fromhome = self.spiderfarfromhome
        

    def writingeffect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()

    #Phase1 Intro Paragraph
    def intropara(self):
        phase3 = r.get(wikiURL)
        soup3 = BeautifulSoup(phase3.content, 'html.parser')
        phase3 = soup3.find_all('p')
        return(self.writingeffect(phase3[1].text))

    #Phase1 Table
    def movieslist(self):
        table = pd.read_html(wikiURL)
        phase3table = (table[2].iloc[:, [0, 1]].copy())
        phase3table.columns = ['Movies Title', 'Release Date']
        phase3table = phase3table.set_index('Movies Title')
        return(phase3table)

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

    def civilwar(self):
        self.infobox(movieurls[0])
        print()
        self.movieplot(movieurls[0])

    def doctorstrange(self):
        self.infobox(movieurls[1])
        print()
        self.movieplot(movieurls[1])

    def gaurdiangalaxytwo(self):
        self.infobox(movieurls[2])
        print()
        self.movieplot(movieurls[2])

    def spiderhomecoming(self):
        self.infobox(movieurls[3])
        print()
        self.movieplot(movieurls[3])

    def thorragnarok(self):
        self.infobox(movieurls[4])
        print()
        self.movieplot(movieurls[4])

    def blackpanther(self):
        self.infobox(movieurls[5])
        print()
        self.movieplot(movieurls[5])

    def infinitywar(self):
        self.infobox(movieurls[6])
        print()
        self.movieplot(movieurls[6])

    def antmanwasp(self):
        self.infobox(movieurls[7])
        print()
        self.movieplot(movieurls[7])

    def captainmarvel(self):
        self.infobox(movieurls[8])
        print()
        self.movieplot(movieurls[8])

    def endgame(self):
        self.infobox(movieurls[9])
        print()
        self.movieplot(movieurls[9])

    def spiderfarfromhome(self):
        self.infobox(movieurls[10])
        print()
        self.movieplot(movieurls[10])

        
thirdwiki = ThePhaseThree()
# thirdwiki.intropara()
# print(thirdwiki.movieslist())
# thirdwiki.civilwar()
# thirdwiki.doctorstrange()
# thirdwiki.gaurdiangalaxytwo()
# thirdwiki.spiderhomecoming()
# thirdwiki.thorragnarok()
# thirdwiki.blackpanther()
# thirdwiki.infinitywar()
# thirdwiki.antmanwasp()
# thirdwiki.captainmarvel()
# thirdwiki.endgame()
# thirdwiki.spiderfarfromhome()