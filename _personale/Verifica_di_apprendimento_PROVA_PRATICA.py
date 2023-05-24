import csv
from pprint import pprint

file_path = ('_personale\Comune-di-Torino---Attivita-commerciali.csv')




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