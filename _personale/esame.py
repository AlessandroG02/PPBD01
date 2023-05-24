import csv
from pprint import pprint

attivita_selezionate = 0
lista_cap = [10126, 10127, 10134]

with open('//Corsi/Dati/Documenti/Corsisti/PPBD01-05/My Documents/corso_python/esame/Comune-di-Torino---Attivita-commerciali.csv', 'r', encoding='utf-8') as foglio_dati:
    lettura = csv.DictReader(foglio_dati, delimiter=';')
  
    for x in lettura:
        
        if  int(x['Anno inizio attivita']) >= 2011:
            if  x['Mq tot locale'].isdigit():
                cap = int(x['Cap'])
                if int(x['Mq tot locale']) >= 150 and cap in lista_cap:
                    attivita_selezionate += 1
pprint(f'Numero di attività commerciali trovate: {attivita_selezionate}')
        

