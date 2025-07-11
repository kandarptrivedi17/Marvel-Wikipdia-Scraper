import requests as r
from bs4 import BeautifulSoup
import time
import sys


class forfans:

    def __init__(self):
        self.first_greet = self.firstgreet
        self.avenger_logo = self.avengerlogo

    def typewriting_effect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()
    
    def firstgreet(self):
        greet = "Greetings, Marvel Fans.I have built a web scraper to extract data from Marvel Cinematic Universe from Wikipedia page. It's about movies from all six phases."
        return (self.typewriting_effect(greet))

    def avengerlogo(self):
        logo = ("""
                ************************************************************************************************************************
                ************************************************************************************************************************
                **********************      ********************************************************************************************
                *********************       ********************************************************************************************
                ********************        ********************************************************************************************
                ************      *         ********************************************************************************************
                *********      ***          ********************************************************************************************
                *******    ******           *****    ***     *         **    ***     **          ***         **           ***         **
                *****    *******     **     ****     **     **         *     **     **          ****         *             *          **
                ****   ********      **     ****     *     **     ******     **     *     *********     ******     **     **     *******
                ***   *********     ***     ****    **    **     ******      *     **     ********     ******     ***    **     ********
                **   *********     ****     ***     *     **     ******            *     *********     ******     **     **    *********
                **   ********     *****     ***          **         **            **    **      *         **      *     **         *****
                **   *******      *******   ***         ***         **           **     **     **         **           ***          ****
                **  *******      ******  *  ***        ***      *****            **    ***     *      *****     **     ****         ****
                **   *****                 ****       ****     ******           **     ***    **     ******    ***     *******     *****
                **   ****                   **       ****     ******     *      *     ***     *     ******     **     ********    ******
                ***   **                  ****       ****         *     **     **     **     **         **    ***     **          ******
                ***   *       ********* *   **      ****         **     **     **            *         **     **     **          *******
                **** **      ***********    **     *****         **    ***    ****         ***         **    ***     **         ********
                ******      *****************    ************************************** ************************************************
                *****      ***************     *****************************************************************************************
                ****      **                 *******************************************************************************************
                ***       ****           ***********************************************************************************************
                ************************************************************************************************************************
                ************************************************************************************************************************
                """)
        print(logo)

    def introduction(self):
        marvel_universe = r.get('https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe')
        soup = BeautifulSoup(marvel_universe.content, 'html.parser')
        intro_para = soup.find_all('p')
        return(self.typewriting_effect(intro_para[2].text))

    def phaseinfobox(self):
        
        url = ('https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe')

        response = r.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        infobox = soup.find('table', class_='infobox plainlist')

        for row in infobox.find_all('tr'):
            cells = row.find_all(['th', 'td'])
            for cell in cells:
                if 'Lists' in cell.text:
                    break
                if 'vte' in cell.text:
                    break
                print(cell.text)

initialgreet = forfans()
initialgreet.firstgreet()
initialgreet.avengerlogo()
initialgreet.introduction()
initialgreet.phaseinfobox()

