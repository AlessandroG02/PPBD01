import pandas as pd
from openpyxl import Workbook
from openpyxl.utils import dataframe
import datetime
from pathlib import Path

date_imput = '15/05/2023'
date_target = datetime.datetime.strptime(date_imput,'%d/%m/%Y')

df_anag = pd.read_excel('./DB C-Lab (HRR).xlsx',    # leggi il file excel
     sheet_name='AnagSkill')                         # legge il foglio anagskill

df_righe_anagskill = df_anag.iloc[[0, 1, 2]]      # estrai le righe dal df

df_candidati = pd.read_excel('./DB C-Lab (HRR).xlsx',    # leggi il file excel
     sheet_name='Candidati')                      # legge il foglio candidati

# filtra solo le righe specificate
filtered_rows = df_candidati[df_candidati['Data invio CV al cliente'].eq(date_target)]
#print(filtered_rows)

df_righe_candidati = df_candidati.iloc[filtered_rows.index]   # estrae le righe dal df
#print(df_righe_2)

filtered_cand_ids = set(df_righe_anagskill['Id candidato'].values)



new_book = Workbook()           # crea un nuovo file excel

new_sheet = new_book.active         # seleziona il foglio di lavoro attivo
new_sheet.title = "AnagSkill"               # crea nuovo foglio anagskill

new_book.create_sheet(title='Candidati')     # crea nuovo foglio candidati 
new_sheet_2 = new_book['Candidati']


# scrivi i dati del dataframe nel foglio di lavoro
for r in dataframe.dataframe_to_rows(df_righe_anagskill, index=False, header=True):
    new_sheet.append(r)

for r in dataframe.dataframe_to_rows(df_righe_candidati, index=False, header=True):
    new_sheet_2.append(r)

# salva il nuovo file excel
new_book.save('./outputs/DB C-Lab (Transfer).xlsx')  

names_cv = []
cv_path = Path('./CV al Cliente/')

file_list = []                                #cerco i cv nella cartella CV
for cognome, nome in names_cv:
    glob_pattern = f'*{cognome} {nome}*'
    cv_trovati = list(cv_path.glob(glob_pattern))
    if len(cv_trovati) == 0:
        raise FileNotFoundError(f'Non è stato trovato il file del CV per la '
                f'persona {cognome} {nome} nella cartella {cv_path}.'
                'Aggiungere il file mancante ed eseguire nuovamente lo script.')
    if len(cv_trovati) == 1:
        file_list += cv_trovati
    else:
        raise FileExistsError(f'Sono stati trovati più file di CV per la '
                f'persona {cognome} {nome} nella cartella {cv_path}.\n'
                'Risolvere il conflitto ed eseguire nuovamente lo script.')
    
print('File di CV trovati:', *[file.name for file in file_list], sep='\n  - ')