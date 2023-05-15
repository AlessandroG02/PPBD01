import pandas as pd
from openpyxl import workbook

df = pd.read_excel('DB C-Lab (Transfer).xlsx',           # leggi il file excel
sheet_name='anagskill')

df_righe = df.iloc[[0, 1, 2]]      # estrai le righe dal data frame

df_foglio = df[['colonna1', 'colonna2']] # estrai il foglio dal dataframe

wb = workbook()           # crea un nuovo file excel

ws = wb.active            # seleziona il foglio di lavoro attivo

#scrivi i dati del dataframe nel foglio di lavoro
for r in dataframe_to_rows(df_righe, index=False, header=True):
    ws.append(r)

wb.save('./_personale/software_per_garzia_completo.xlsx')  #salva il file excel



