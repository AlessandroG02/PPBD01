# import csv

# identifier = 'ID'                                       # identificatore dei record
# col_names = ['ID', 'Ragione sociale', 'Comune', 'Cap']  # colonne da estrarre
# record_ids = [45, 64, 176, 204]                         # record da estrarre
# sep_rec = '----------------------------'                # separatore visivo da usare

# tot_comuni = 0
# tot_abitanti = 0

# with open('./files_esercizi/Sardegna_centri_urbani_per_abitante_e_altitudine_2014-01-13.csv',
#           encoding='latin-1') as file_in:
#     reader_obj = csv.DictReader(file_in, delimiter=';')  # ottengo una lista di liste (come iterabile)
#     next(reader_obj)             # salto la prima riga, dove c'è l'intestazione
#     for linea in reader_obj:
#         if linea[identifier] in [str(idn) for idn in record_ids]:  # filtro
#             for col_name in col_names:
#                 print(col_name+':', linea[col_name])
#             print(sep_rec)
#         else:
#             pass

# print('N. centri urbani sopra i 600 m s.l.m.:', tot_comuni)
# print('N. abitanti sopra i 600 m s.l.m.:', tot_abitanti)


#-------------------------------------------------------------------------------
#ALTERNATIVA
#-------------------------------------------------------------------------------


import csv

tot_comuni = 0
tot_abitanti = 0

with open('./files_esercizi/Sardegna_centri_urbani_per_abitante_e_altitudine_2014-01-13.csv',
          encoding='latin-1') as file_in:
    reader_obj = csv.DictReader(file_in, delimiter=';') # trasformiamo ogni riga in un dizionario
                                                        #    e ottengo una lista di dizionari (come mappatura iterabile)
    for linea in reader_obj:                            # per ciascuno di questi dizionari (che son i record/comuni)
        if int(linea["QUOTA LOCALITA'"]) > 600:         # se il valore alla chiave "QUOTA LOCALITA'" è maggiore di 600
                                                        # accedo al valore con la chiave anziché con l'indice
            tot_comuni += 1                             # incrementa il contatore dei comuni di 1
            tot_abitanti += int(linea["ABITANTI LOCALITA'"])  # incrementa il contatore abitanti del numero di
                                                              #    abitanti indicati alla chiave "ABITANTI LOCALITA'"

print('N. centri urbani sopra i 600 m s.l.m..:', tot_comuni)
print('N. abitanti sopra i 600 m s.l.m.:', tot_abitanti)