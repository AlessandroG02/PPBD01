import pandas as pd
import os
import shutil
import base64
from email import encoders
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import NamedStyle

# sopprime gli errori che riguardano le estensioni dei dati contenuti nei fogli excel
import warnings

warnings.simplefilter("ignore")

# input data del lavoro che vogliamo inviare
data_invio = input('Inserire la (dd/mm/yyyy) data dei lavori che si desiderano inviare: ')
from datetime import datetime

try:
    date = datetime.strptime(data_invio, "%d/%m/%Y").date()
except ValueError:
    print("La data inserita non è nel formato corretto.")
    exit()

if not date:
    print('Inserire una data valida')
    exit()
else:
    # apre foglio candidati
    file_path = "/ACE10001I C-Lab HR/DB C-Lab (HRR).xlsx"

    if not os.path.exists(file_path):
        print(f"Il file {file_path} non esiste.")
        exit()

    foglio_candidati = pd.read_excel(file_path, sheet_name='Candidati')

    # localizziamo le righe che contengono la data
    posizione_data = foglio_candidati[foglio_candidati.eq(data_invio).any(axis=1)]

    # Controllo sulla presenza di righe da copiare
    if posizione_data.empty:
        print("Non ci sono righe da copiare per la data specificata.")
        exit()

    # copiare le righe che ci interessano nel file da inviare
    righe_da_copiare = foglio_candidati.loc[posizione_data.index]
    new_file_path = "/ACE10001I C-Lab HR/DB C-Lab_(Transfer).xlsx"
    righe_da_copiare.to_excel(new_file_path, index=False, sheet_name='Candidati')

    # cercare nel foglio anagskill i dati dei candidati selezionati
    foglio_anagskill = pd.read_excel(file_path, sheet_name='AnagSkill')
    anagskill_transfer = pd.DataFrame()
    nomi_curriculum = []
    percorsi_cv = []

    for riga, row in righe_da_copiare.iterrows():
        identificativo_candidato = row['Id candidato']

        for y, q in foglio_anagskill.iterrows():
            valore = q['Progr Interno']

            if valore == identificativo_candidato:
                anagskill_transfer = pd.concat([anagskill_transfer, q], axis=1)
                cognome = q['Cognome']
                nome = q['Nome']
                cognome_nome = cognome + ' ' + nome
                percorso_cv = 'C:/Users/Utente/Documents/Progetto_Garzia/ACE10001I C-Lab HR/CV al Cliente/' + cognome_nome + ' (Fabio).docx'
                print(percorso_cv)

                if not os.path.exists(percorso_cv):
                    print(f"Il file {percorso_cv} non esiste.")
                    exit()

                if cognome_nome not in nomi_curriculum:
                    nomi_curriculum.append(cognome_nome)
                    percorsi_cv.append(percorso_cv)

                print(nomi_curriculum)

    with pd.ExcelWriter(new_file_path, mode='a') as writer:
        anagskill_transfer.transpose().to_excel(writer, index=False, sheet_name='AnagSkill')

    # Definisci il percorso completo della cartella di destinazione
    percorso_destinazione = "C:/Users/Utente/Documents/Progetto_Garzia/ACE10001I C-Lab HR/Cartella_Destinazione/"



    # Controllo sull'esistenza della cartella di destinazione
    if not os.path.exists(percorso_destinazione):
        print(f"La cartella di destinazione {percorso_destinazione} non esiste.")
        exit()

    # Sposta i file CV nella cartella di destinazione
    for percorso_cv in percorsi_cv:
        percorso_cv_destinazione = os.path.join(percorso_destinazione, os.path.basename(percorso_cv))
        shutil.copy(percorso_cv, percorso_cv_destinazione)

    # Sposta il file Excel nella cartella di destinazione
    new_file_path_destinazione = os.path.join(percorso_destinazione, os.path.basename(new_file_path))
    shutil.copy(new_file_path, new_file_path_destinazione)
    nome_ultima_cartella = os.path.basename(os.path.dirname(new_file_path_destinazione))
    print(f'I file sono stati spostati nella cartella {nome_ultima_cartella}')





# automatizzazione mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# Parametri di configurazione per l'invio della mail
smtp_server = 'smtp.libero.it'
smtp_port = 587
sender_email = 'indirizzohrr@libero.it'
sender_password = 'indHRR23+'
receiver_email = 'sedecentrale_2023@libero.it'
subject = 'Candidati'
body = """Alla cortese attenzione della Sede Centrale,
in allegato i file relativi ai candidati selezionati per le richieste ricevute.

Cordiali saluti"""

# Crea il messaggio
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Funzione per allegare i file
def attach_file(filename):
    with open(filename, 'rb') as file:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(file.read())
        # Rinomina il nome del file utilizzando solo il nome del file
        file_name = os.path.basename(filename)
        attachment.add_header('Content-Disposition', 'attachment', filename=file_name)

        # Codifica il payload in base64 utilizzando il modulo email.encoders
        encoders.encode_base64(attachment)

        message.attach(attachment)

# Allega i file
for cognome_nome in nomi_curriculum:
    print(cognome_nome)
       # personalizzare il nome del file cv in modo che alleghi il cv di ciascun candidato
    #percorso_cv = f'C:/Users/Utente/Documents/Progetto_Garzia/ACE10001I C-Lab HR/Cartella_Destinazione/cv_{cognome_nome}.pdf'
    attach_file(f'C:/Users/Utente/Documents/Progetto_Garzia/ACE10001I C-Lab HR/Cartella_Destinazione/{cognome_nome} (Fabio).docx')
    

attach_file("/ACE10001I C-Lab HR/Cartella_Destinazione/DB C-Lab_(Transfer).xlsx")



try:
    # Connessione al server SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Invio della mail
    server.send_message(message)
    print("Mail inviata con successo!")

except Exception as e:
    print("Si è verificato un errore durante l'invio della mail:", str(e))

finally:
    # Chiusura della connessione
    server.quit()

import imaplib
import email
from bs4 import BeautifulSoup

# Credenziali per l'account mail.com
username = 'momo_edo_python@outlook.com'
password = '!Torino23!'

# Connettiti al server IMAP di Outlook
mail = imaplib.IMAP4_SSL('Outlook.office365.com', 993)

# Effettua il login
mail.login(username, password)

# Seleziona la casella di posta in arrivo
mail.select('inbox')

# Cerca le email nella casella di posta in arrivo
result, data = mail.search(None, 'ALL')

# Otteniamo l'ID dell'ultima email ricevuta
email_ids = data[0].split()
latest_email_id = email_ids[-1]

# Otteniamo il corpo dell'email
result, email_data = mail.fetch(latest_email_id, '(RFC822)')
raw_email = email_data[0][1]

# Parsing del contenuto dell'email
msg = email.message_from_bytes(raw_email)

# Estrai il contenuto del corpo del messaggio
if msg.is_multipart():
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            body = part.get_payload(decode=True).decode('utf-8')
            break
else:
    body = msg.get_payload(decode=True).decode('utf-8')

# Chiudi la connessione con il server IMAP
mail.logout()

# Effettua il parsing dell'HTML
soup = BeautifulSoup(body, 'html.parser')

# Trova la tabella con il tag specificato
table = soup.find('table', {'border': '0', 'cellspacing': '0', 'cellpadding': '0', 'width': '1313'})

# Estrai i dati dalla tabella
data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.get_text(strip=True))
    data.append(row_data)

# Crea il dataframe con i dati estratti
df = pd.DataFrame(data)

# Crea il file Excel
output_file = '../dati.xlsx'
df.to_excel(output_file, index=False)

print("File Excel creato con successo: ", output_file)