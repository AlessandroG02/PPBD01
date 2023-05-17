import pandas as pd
import xlsxwriter
import openpyxl
import datetime



data_invio = input('Si prega di inserire la data di inserimento dei candidati: ')
from datetime import datetime
date = datetime.strptime(data_invio, "%d/%m/%Y")
if not date:
    print('si prega di inserire una data valida')

df_path_hrr = (r"C:\Users\andre\Desktop\ACE10001I C-Lab HR\DB_C-Lab_(HRR).xlsx")
df_candidati = pd.read_excel(df_path_hrr, sheet_name= 'Candidati')

date_location = df_candidati[df_candidati.eq(data_invio).any(axis=1)]

lines_to_copy = df_candidati.iloc[date_location.index]

df_path_transfer = (r"C:\Users\andre\Desktop\ACE10001I C-Lab HR\DB_C-Lab_(Transfer).xlsx")
df_path_transfer.to_excel(df_path_transfer, index=False, sheet_name='Candidati')
