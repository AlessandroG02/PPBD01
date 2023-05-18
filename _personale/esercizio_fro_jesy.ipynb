# 
# get system data and save into sy_date

# from datetime import date
# today_date = date.today()
# dd/mm/YY
# sy_date = today_date.strftime("%d/%m/%Y")
# print(today_date)
# read file

import os
import openpyxl
# import sys

dirname = os.path.dirname(__file__)
worbook_path = os.path.join(dirname, '../ACE10001I C-Lab HR/DB C-Lab (HRR2).xlsx')

internal_file = openpyxl.load_workbook(worbook_path, read_only=True, data_only=True)
# print('workbook_loaded')
# lista_nomi_fogli = internal_file.sheetnames
# print(lista_nomi_fogli)
# go to sheet "candidati"
# check lines, if empty return a warning
# print(sh_candidati.max_row)

print('Read Candidati')
sh_candidati = internal_file['Candidati']
candidati_matched_rows = []
for row_id in range(2, sh_candidati.max_row+1):
    if sh_candidati.cell(row=row_id, column=20).value == "CV al Cliente":
        row = []
        for col_id in range(1,sh_candidati.max_column):
            cell = sh_candidati.cell(row=row_id, column=col_id).value
            row.append(cell)
        candidati_matched_rows.append(row)
print(candidati_matched_rows)


print('Read AnagSkill')
sh_anagrafica = internal_file['AnagSkill']
anagrafica_matched_rows = []
for anagrafica_row_id in range(2, sh_anagrafica.max_row):
    prog_interno = sh_anagrafica.cell(row=anagrafica_row_id, column=2).value
    if prog_interno == None:
        break
    for candidati_row in candidati_matched_rows:        
        if prog_interno == candidati_row[7]:
            # print(sh_anagrafica.cell(row=anagrafica_row_id, column=2).value)
            row = []
            for col_id in range(1,sh_candidati.max_column):
                cell = sh_anagrafica.cell(row=anagrafica_row_id, column=col_id).value
                row.append(cell)
            anagrafica_matched_rows.append(row)  
            break      
print(anagrafica_matched_rows)

