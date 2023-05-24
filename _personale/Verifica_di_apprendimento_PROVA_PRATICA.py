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