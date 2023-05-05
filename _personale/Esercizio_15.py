"""
Le età dei nostri amici
Requisiti: import, with ... as, open, dict

E’ dato un file nomi_data_nascita.txt nella cartella /files_esercizi del nostro repository. Il file è caratterizzato dal seguente formato rappresentante delle coppie nome/età. Per esempio:

Ada: 1999
Pippo: 1980
Felice: 1976
Geronima: 1999
...
Leggi tutto il file creando un dizionario (dict) le cui chiavi sono corrispondono all’età della persona alla data attuale. A ciascuna età deve essere associata una lista con i nomi di persone che hanno quell’età.

Output atteso:

{24: ['Ada:', 'Geronima:', 'Roberto:'], 43: ['Pippo:', 'Ciccio:'], 47: ['Felice:', 'Mimmo:'], 51: ['Luca:', 'Pluto:'], 100: ['Totò:']}
# scrivi qui
Ora, riesci a scriverle in un file nuovo, mantenendo il seguente formato?

Nome,Età
Ada,24
Geronima,24
Roberto,24
Pippo,43
Ciccio,43
...
Prova a scrivere un nuovo file nomi_eta.csv nella cartella /files_esercizi del nostro repository.

Normalmente i file .csv hanno la prima linea dedicata alle "intestazioni di colonna". In questo caso nella prima riga del file dovremmo avere Nome,Età.

# scrivi qui
Per finire, riusciresti a creare uno script che prende in ingresso due parametri, il file di origine nomi_data_nascita.txt e il file di output nomi_eta.csv e che esegue le conversione creando il file di output?

Per lanciare il nostro script, immaginando di trovarci nella cartella /files_esercizi, dovremmo poter lanciare un comando come il seguente:

$ py converti_nomi_nascita.py nomi_data_nascita.txt nomi_eta.csv
Crea un nuovo file e chiamalo converti_nomi_nascita.py e salvalo dove preferisci, per esempio nella tua cartella /personale che dovresti avrere sul tuo branch del nostro repository.

Ricorda che poi i percorsi ai file devono essere compatibili con la posizione in cui eseguirai lo script, dove tu ti trovi e dove si trova il file da convertire. Prova varie combinazioni, e vedi cosa succede e dove viene generato il file di output.
"""

import datetime

# apre il file in lettura
with open("files_esercizi/nomi_data_nascita.txt", "r") as f:
    # crea un dizionario vuoto
    age_dict = {}
    # legge il file riga per riga
    for line in f:
        # divide la riga in nome ed età
        name, birthyear = line.strip().split(": ")
        # calcola l'età della persona alla data attuale
        age = datetime.date.today().year - int(birthyear)
        # se l'età non esiste come chiave nel dizionario, la aggiunge con una lista vuota
        if age not in age_dict:
            age_dict[age] = []
        # aggiunge il nome alla lista corrispondente all'età
        age_dict[age].append(name + ":")

# crea un nuovo file in scrittura
with open("files_esercizi/nomi_eta.csv", "w") as f:
    # scrive la riga di intestazione
    f.write("Nome,Età\n")
    # scorre il dizionario in ordine crescente di età
    for age in sorted(age_dict):
        # scrive ogni nome ed età nel file, separati da una virgola
        for name in age_dict[age]:
            f.write(f"{name},{age}\n")
