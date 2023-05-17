import pandas as pd


#sopprime gli errori che riguardano le estensioni dei dati contenuti nei fogli excel
import warnings
warnings.simplefilter("ignore")

# input data del lavoro che vogliamo inviare
data_invio = input('Inserire la (dd/mm/yyyy) data dei lavori che si desiderano inviare: ')
from datetime import datetime
date = datetime.strptime(data_invio, "%d/%m/%Y")
if not date:
    print('inserire una data valida')
else:
    # apre foglio candidati
    file_path = "//Corsi/Dati/Documenti/Corsisti/PPBD01-05/Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(HRR).xlsx"
    foglio_candidati = pd.read_excel(file_path, sheet_name= 'Candidati')
    # localizziamo le righe che contengono la data
    posizione_data = foglio_candidati[foglio_candidati.eq(data_invio).any(axis=1)]
    # copiare le righe che ci interessano nel file da inviare
    righe_da_copiare = foglio_candidati.loc[posizione_data.index]
    new_file_path = "//Corsi/Dati/Documenti/Corsisti/PPBD01-05/Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(Transfer).xlsx"
    righe_da_copiare.to_excel(new_file_path, index=False, sheet_name='Candidati')
    
    # cercare nel foglio anagskill i dati dei candidati selezionati
    foglio_anagskill = pd.read_excel(file_path, sheet_name= 'AnagSkill')
    anagskill_transfer = pd.DataFrame()
    for riga, row in righe_da_copiare.iterrows():
        identificativo_candidato = row['Id candidato']
        for y, q in foglio_anagskill.iterrows():
            valore = q['Progr Interno']
            if valore == identificativo_candidato:
                anagskill_transfer = anagskill_transfer.append(q)
                cognome = q['Cognome']
                nome = q['Nome']
                cognome_nome = cognome + '_' + nome
                nomi_curriculum = []
                percorso_cv = 'C:/Users/Chay/Desktop/ACE10001_C-Lab_HR/CV al Cliente/CV/cv_' + cognome_nome + '.pdf'
                print(percorso_cv)
                
    with pd.ExcelWriter(new_file_path, mode='a') as writer:
        anagskill_transfer.to_excel(writer, index=False, sheet_name= 'AnagSkill')


# automatizzazione mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# Parametri di configurazione per l'invio della mail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'indirizzo_HRR@gmail.com'
sender_password = 'password'
receiver_email = 'Sede_Centrale@gmail.com'
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
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(attachment)

# Allega i file
attach_file('C:/Users/Chay/Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(Transfer).xlsx')
# personalizzare il nome del file cv in modo che alleghi il cv di ciascun candidato
for nome in nomi_curriculum:
    percorso_cv = 'C:/Users/Chay/Desktop/ACE10001_C-Lab_HR/CV al Cliente/CV/cv_' + cognome_nome + '.pdf'
    attach_file(percorso_cv)

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

