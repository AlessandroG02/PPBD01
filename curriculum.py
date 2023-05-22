import pandas as pd
import datetime
# Ignoro gli avvisi di errori nei file excel
import warnings
warnings.simplefilter("ignore")

# Setto i path dei file xlsx
path_db = 'C:/Users/kpani/Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(HRR).xlsx'
path_transfer = 'C:/Users/kpani/Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(Transfer).xlsx'

# Leggi il foglio Candidati
candidati = pd.read_excel(path_db, sheet_name= 'Candidati')

# Chiedi all'utente di inserire una data in formato dd/gg/yyyy e la converto in un oggetto
user_date = input("Inserisci una data in formato dd/gg/yyyy: ")
user_date = datetime.datetime.strptime(user_date, "%d/%m/%Y")

# Formatto la data in una stringa con il formato yyyy-mm-dd
user_date = user_date.strftime("%Y-%m-%d")

# Seleziona le righe che contengono la data inserita dall'utente e le copio
righe_selezionate = candidati[candidati.eq(user_date).any(axis=1)]
copia_righe = candidati.loc[righe_selezionate.index]

# Scrivo le righe selezionate nel file excel DB_C-Lab_(Transfer) nel foglio Candidati
copia_righe.to_excel(path_transfer, index=False, sheet_name="Candidati")

# Stampa le righe selezionate
print(copia_righe)