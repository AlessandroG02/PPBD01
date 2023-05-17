from datetime import datetime
print(datetime.today().strftime('%d-%m-%y'))

import openpyxl
data_transfer = openpyxl.load_workbook(r'\\corsi\Dati\Documenti\Corsisti\PPBD01-03\My Documents\corso_python\PPBD01\Progetto-Garzia\DB C-Lab (Transfer).xlsx')
lista_fogli = data_transfer.sheetnames
foglio_candidati = data_transfer['Candidati'] 
print(foglio_candidati)
