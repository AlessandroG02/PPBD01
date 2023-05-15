import pandas as pd
from openpyxl import workbook

df = pd.read_excel('DB C-Lab (HRR).xlsx',           # leggi il file excel
sheet_name='AnagSkill')

df_righe = df.iloc[[0, 1, 2]]      # estrai le righe dal data frame

new_book = workbook()           # crea un nuovo file excel
new_sheet = new_book.active         # seleziona il foglio di lavoro attivo

new_sheet.title = "crezione_file_xlsx"

# scrivi i dati del dataframe nel foglio di lavoro
for r in dataframe_to_rows(df_righe, index=False, header=True):
    new_sheet.append(r)

# salva il file excel
new_book.save('./_personale/software_per_garzia_completo.xlsx')  