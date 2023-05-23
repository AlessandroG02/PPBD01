import csv

tot_comuni = 0
tot_abitanti = 0

with open('../../files_esercizi/Sardegna_centri_urbani_per_abitante_e_altitudine_2014-01-13.csv',
          encoding='latin-1') as file_in:
    reader_obj = csv.reader(file_in, delimiter=';')  # ottengo una lista di liste (come iterabile)
    next(reader_obj)             # salto la prima riga, dove c'è l'intestazione
    for linea in reader_obj:     # per ciascuna lista (la riga, che corrisponde a un record/comune)
        if int(linea[5]) > 600:  # se il valore nella sesta colonna (index 5) è maggiore di 600
            tot_comuni += 1      # incrementa il contatore dei comuni di 1
            tot_abitanti += int(linea[4])  # incrementa il contatore abitanti del numero di
                                           #    abitanti del comune corrente (colonna 5, index 6)

print('N. centri urbani sopra i 600 m s.l.m.:', tot_comuni)
print('N. abitanti sopra i 600 m s.l.m.:', tot_abitanti)