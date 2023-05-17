from datetime import datetime
print(datetime.today().strftime('%d-%m-%y'))

import openpyxl
data_transfer = openpyxl.load_workbook(r'\\corsi\Dati\Documenti\Corsisti\PPBD01-03\My Documents\corso_python\PPBD01\Progetto-Garzia\DB C-Lab (HRR).xlsx', read_only=True, data_only=True)
foglio_candidati = data_transfer['Candidati']
print(foglio_candidati)



