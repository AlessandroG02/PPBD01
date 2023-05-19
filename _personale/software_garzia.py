import pandas as pd
from openpyxl import Workbook
from openpyxl.utils import dataframe

df_anag = pd.read_excel('progetti/xlsx/DB C-Lab (HRR).xlsx',    # leggi il file excel
     sheet_name='AnagSkill')                         # legge il foglio anagskill

df_righe = df_anag.iloc[[0, 1, 2]]      # estrai le righe dal data frame

df_candidati = pd.read_excel('progetti/xlsx/DB C-Lab (HRR).xlsx',    # leggi il file excel
     sheet_name='Candidati')                         # legge il foglio candidati

df_righe_2 = df_candidati.iloc[[0, 1, 2]] 


new_book = Workbook()           # crea un nuovo file excel

new_sheet = new_book.active         # seleziona il foglio di lavoro attivo
new_sheet.title = "AnagSkill"

new_book.create_sheet(title='Candidati')
new_sheet_2 = new_book['Candidati']


# scrivi i dati del dataframe nel foglio di lavoro
for r in dataframe.dataframe_to_rows(df_righe, index=False, header=True):
    new_sheet.append(r)

for r in dataframe.dataframe_to_rows(df_righe_2, index=False, header=True):
    new_sheet_2.append(r)

# salva il file excel
new_book.save('./_personale/DB C-Lab (Transfer).xlsx')  