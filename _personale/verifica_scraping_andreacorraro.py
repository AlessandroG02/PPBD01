import requests
from pprint import pprint
from bs4 import BeautifulSoup

url_base = 'https://www.scrapethissite.com/pages/simple/'

result = requests.get(url_base)

if result.status_code == 200:
    soup = BeautifulSoup(result.content, 'html.parser')

    countries = soup.select('div.country')


       
    items= []

    for adv in countries:
            data = {
            'nome' : adv.select('h3[class~=country-name]'),
            'capitale' : adv.select('span[class~=country-capital]'),
            'popolazione' : adv.select('span[class~=country-population]'),
            'area' : adv.select('span[class~=country-area]'),
            }

            for key, value in data.items():
                if value:
                # Se l'elemento è presente, estrai il testo
                   data[key] = value[0].get_text().strip()
                else:
                    # Se l'elemento non è presente, imposta il valore a None
                    data[key] = None
        
            items.append(data)

    # Stampa i dati estratti
    pprint(items)
           