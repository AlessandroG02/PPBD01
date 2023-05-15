<<<<<<< HEAD
from openpyxl import Workbook

nuovo_book = Workbook()          # creo l'oggetto per interfacciarmi col workbook
nuovo_sheet = nuovo_book.active  # seleziono il worksheet attivo

nuovo_sheet.title = "creazione_file_xlsx"

# scrivo i dati uno alla volta
nuovo_sheet['A1'] = 'gatto'
nuovo_sheet['A2'] = 'cane'
nuovo_sheet['A3'] = 'pappagallo'
nuovo_sheet['A4'] = 'criceto'

# salvo il file (come fare un "flush")
nuovo_book.save('./_personale/nuovo_file.xlsx')