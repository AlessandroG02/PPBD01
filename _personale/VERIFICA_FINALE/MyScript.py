import csv

def conta_attivita_commerciali(file_path, anno_minimo, superficie_minima, cap_interessati):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        conteggio = 0
        for row in reader:
            anno_inizio = row['Anno inizio attivita']
            superficie = row['Mq tot locale']
            cap = row['Cap']
            
            if anno_inizio.isdigit() and int(anno_inizio) >= anno_minimo and \
               superficie.replace('.', '').isdigit() and int(superficie.replace('.', '')) >= superficie_minima and \
               cap in cap_interessati:
                conteggio += 1
        
        return conteggio


file_path = "_personale/VERIFICA_FINALE/Comune-di-Torino---Attivita-commerciali.csv"
anno_minimo = 2011
superficie_minima = 150
cap_interessati = ['10126', '10127', '10134']

risultato = conta_attivita_commerciali(file_path, anno_minimo, superficie_minima, cap_interessati)

print("Numero di attività commerciali trovate:", risultato)
