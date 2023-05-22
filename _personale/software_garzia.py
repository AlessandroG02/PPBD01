import pandas as pd
from openpyxl import Workbook
from openpyxl.utils import dataframe
import datetime

date_imput = '15/05/2023'
date_target = datetime.datetime.strptime(date_imput,'%d/%m/%Y')

df_anag = pd.read_excel('progetti/xlsx/DB C-Lab (HRR).xlsx',    # leggi il file excel
     sheet_name='AnagSkill')                         # legge il foglio anagskill

df_righe = df_anag.iloc[[0, 1, 2]]      # estrai le righe dal data frame

df_candidati = pd.read_excel('progetti/xlsx/DB C-Lab (HRR).xlsx',    # leggi il file excel
     sheet_name='Candidati')                         # legge il foglio candidati

# filtra solo le righe specificate
filtered_rows = df_candidati[df_candidati['Data invio CV al cliente'].eq(date_target)]
#print(filtered_rows)

df_righe_2 = df_candidati.iloc[filtered_rows.index] 
#print(df_righe_2)

filtered_cand_id = df_righe_2['Id candidato']
#print(filtered_cand_id)



new_book = Workbook()           # crea un nuovo file excel

new_sheet = new_book.active         # seleziona il foglio di lavoro attivo
new_sheet.title = "AnagSkill"               # crea nuovo foglio anagskill

new_book.create_sheet(title='Candidati')     # crea nuovo foglio candidati 
new_sheet_2 = new_book['Candidati']


# scrivi i dati del dataframe nel foglio di lavoro
for r in dataframe.dataframe_to_rows(df_righe, index=False, header=True):
    new_sheet.append(r)

for r in dataframe.dataframe_to_rows(df_righe_2, index=False, header=True):
    new_sheet_2.append(r)

# salva il nuovo file excel
new_book.save('./_personale/DB C-Lab (Transfer).xlsx')  