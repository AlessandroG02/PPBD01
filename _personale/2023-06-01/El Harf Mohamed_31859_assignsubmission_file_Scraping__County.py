import requests
from bs4 import BeautifulSoup
import csv


# Funzione per l'estrazione dei dati dalla pagina
def scrape_page(url):
    # Effettuo la richiesta HTTP GET alla pagina
    response = requests.get(url)

    # Analizzo il contenuto HTML della pagina con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trovo tutti i div con la classe "col-md-4 country"
    countries = soup.find_all('div', class_='col-md-4 country')

    # Lista per immagazzinare i dati estratti
    data = []

    # Iter *Ciclo* sui div delle nazioni
    for country in countries:
        # Estraggo il nome della nazione
        name = country.find('h3', class_='country-name').text.strip()

        # Estraggo la capitale
        capital = country.find('span', class_='country-capital').text.strip()

        # Estrago la popolazione
        population = country.find('span', class_='country-population').text.strip()

        # Estraggo l'area
        area = country.find('span', class_='country-area').text.strip()

        # Aggiungo i dati alla lista
        data.append({
            'Nome': name,
            'Capitale': capital,
            'Popolazione': population,
            'Area': area
        })

    return data


# URL della pagina da cui effettuare lo scraping
url = 'https://www.scrapethissite.com/pages/simple/'

# Eseguo lo scraping della pagina
scraped_data = scrape_page(url)

# Stampo i dati estratti
for item in scraped_data:
    print(item)

# Scrivo i dati estratti in un file CSV
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Nome', 'Capitale', 'Popolazione', 'Area']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    writer.writerows(scraped_data)
