from bs4 import BeautifulSoup
import requests

def phases():
    url = ('https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe')

    response = requests.get(url)

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

