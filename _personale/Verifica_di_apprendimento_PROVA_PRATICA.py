<<<<<<< HEAD
import csv
from pprint import pprint

file_path = 'Comune-di-Torino---Attivita-commerciali.csv'




def conta_attività(pathFile):
    counter = 0
    anno = 2011
    sup = 150
    zone = [10126, 10127, 10134]
    with open(pathFile, encoding='latin-1') as filex:
        readable_obj = csv.DictReader(filex, delimiter= ';')
        for attività in readable_obj:
            if attività['Mq tot locale'].isdigit():
                annoInizio = int(attività['Anno inizio attivita'])
                capLocale = int(attività['Cap'])
                mqLocale = int(attività['Mq tot locale'])
                if annoInizio >= anno and mqLocale >= sup and capLocale in zone:
                    counter += 1
    print(f'Numero attività commerciali trovate: {counter}')

conta_attività(file_path)
=======
# scrivi qui
import json
from pprint import pprint
counter=0
lista_cap=["10126", "10127","10134"]
file_path='C:/Users/Utente/OneDrive/Documents/PPBD01/_personale/Comune-di-Torino---Attivita-commerciali.json'
surf=150

with open(file_path,
          encoding='latin-1') as file_in:
            reader_obj = json.load(file_in)
            for attivita in reader_obj:
                        if attivita['Mq tot locale'].isdigit():
                          if int(attivita['Anno inizio attivita'])>=2011 and int(attivita['Mq tot locale'])>=surf and attivita['Cap'] in lista_cap:
                                counter+=1
pprint(f"Numero attività commerciali trovate: {counter}")   
>>>>>>> 24811b8eddcc5a228454093b798119dc93913015
