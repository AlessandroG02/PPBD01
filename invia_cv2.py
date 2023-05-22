# Importo i moduli necessari
import pandas as pd
import datetime
import warnings
import os

# Ignoro gli avvisi di errori nei file excel
warnings.simplefilter("ignore")

# Setto la variabile di ambiente User e setto il path dei file xlsx e pdf
userprofile = os.environ.get("userprofile")
path_db = os.path.join("C:/Users", userprofile, "Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(HRR).xlsx")
path_transfer = os.path.join("C:/Users", userprofile, "Desktop/ACE10001_C-Lab_HR/DB_C-Lab_(Transfer).xlsx")

def seleziona_e_copia_righe(path_db, path_transfer):
    """Seleziona e copia le righe del foglio Candidati che contengono una data inserita dall'utente.

    Parametri:
    path_db (str): il path del file excel DB_C-Lab_(HRR)
    path_transfer (str): il path del file excel DB_C-Lab_(Transfer)

    """
    try:
        # Leggo il foglio Candidati
        candidati = pd.read_excel(path_db, sheet_name='Candidati')

        # Chiedo all'utente di inserire una data in formato dd/gg/yyyy e la converto in un oggetto
        user_date = input("Inserisci una data in formato dd/gg/yyyy: ")
        user_date = datetime.datetime.strptime(user_date, "%d/%m/%Y")

        # Formatto la data in una stringa con il formato yyyy-mm-dd
        user_date = user_date.strftime("%Y-%m-%d")

        # Seleziono le righe che contengono la data inserita dall'utente e le copio
        righe_selezionate = candidati[candidati.eq(user_date).any(axis=1)]
        copia_righe = candidati.loc[righe_selezionate.index]

        # Scrivo le righe selezionate nel file excel DB_C-Lab_(Transfer) nel foglio Candidati
        copia_righe.to_excel(path_transfer, index=False, sheet_name="Candidati")

        # Leggo il file excel che contiene il foglio anagskill
        anagskill = pd.read_excel(path_db, sheet_name="AnagSkill")

        anagskill_df = pd.DataFrame(columns=anagskill.columns)
        # Create an empty list to store the rows
        rows = []

        # Loop through the rows of copia_righe
        for riga, row in copia_righe.iterrows():
            id = row['Id candidato']
            # Loop through the rows of anagskill
            for y, q in anagskill.iterrows():
                id2 = q['Progr Interno']
                if id2 == id:
                # Append the matching row to anagskill_df
                    anagskill_df = pd.concat([anagskill_df, q.to_frame().T])
                    print(anagskill_df)
                    cognome = q['Cognome']
                    nome = q['Nome']
                    # Incollo il Nome e Cognome
                    cognome_nome = cognome + '_' + nome
                    
                    # Creo una Lista di risultati trovato
                    nomi_curriculum = []
                    # Creo il Path del PDF da allegare
                    path_cv = os.path.join("C:/Users", userprofile, "Desktop/ACE10001_C-Lab_HR/CV al Cliente/CV/cv_' + cognome_nome + '.pdf'")
                    print(path_cv)

                    #with pd.ExcelWriter(path_transfer, mode='a') as writer:
                    #    anagskill_df.to_excel(writer, index=False, sheet_name= 'AnagSkill')

                    import openpyxl

                    with pd.ExcelWriter(path_transfer, engine='openpyxl', mode='a') as writer:
                        anagskill_df.to_excel(writer, index=False, sheet_name='AnagSkill')


                    # Importo i moduli necessari per inviare la mail
                    #import smtplib
                    #from email.message import EmailMessage

                    # Definisco i parametri della mail
                    #sender = "mail.lunodesign@gmail.com"
                    #receiver = "kpanik@gmail.com"
                    #subject = "Curriculum"
                    #body = "This is a test email with a pdf and an excel file attached."
                    #pdf_file = path_cv
                    #excel_file = path_transfer
                    #pdf_file = path_cv

                    # Crea un messaggio di posta elettronica
                    #msg = EmailMessage()
                    #msg["From"] = sender
                    #msg["To"] = receiver
                    #msg["Subject"] = subject
                   # msg.set_content(body)

                    # Allego il file PDF
                    #with open(pdf_file, "rb") as f:
                    #    file_data = f.read()
                    #    file_name = os.path.basename(f.name)
                    #    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

                    # Allego il file EXCEL
                    #with open(excel_file, "rb") as f:
                    #    file_data = f.read()
                    #    file_name = os.path.basename(f.name)
                    #    msg.add_attachment(file_data, maintype="application", subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=file_name)

                    # Creo l'oggetto SMTP e invio la mail
                    #with smtplib.SMTP_SSL("smtp.gmail.com", 587) as smtp:
                        # Attivo il protocollo SSL alla porta 587 con ehlo e starttls altrimenti rem
                    #    smtp.ehlo()
                    #    smtp.starttls()
                        # Effettuo il login con la mia mail
                    #    smtp.login(sender, "luno10design2030")
                        # Invio la mail
                    #    smtp.send_message(msg)
                        # Stampo un messaggio di conferma
                    #    print("La mail è stata inviata con successo")

        # Stampo le righe selezionate
        print(copia_righe)
    
    #except ValueError:
    #    print("La data inserita non è valida. Riprova con un formato corretto.")
    
    except FileNotFoundError:
        print("Uno o entrambi i file excel non sono stati trovati. Controlla i path.")

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, recipient_email, subject, message, attachments=None):
    # Crea l'oggetto del messaggio
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Aggiunge il corpo del messaggio
    msg.attach(MIMEText(message, 'plain'))

    # Aggiunge gli allegati, se presenti
    if attachments:
        for attachment in attachments:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attachment, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{attachment}"')
            msg.attach(part)

    # Connette al server SMTP di Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Invia il messaggio
    server.send_message(msg)
    server.quit()



    

# Specifica gli allegati, se necessario
attachments = [path_transfer]
# Esempio di utilizzo
sender_email = 'prova.test.camerana@gmail.com'
sender_password = 'Ppbd01!!!'
recipient_email = 'kpanik@gmail.com'
subject = 'Curriculum Candidati'
message = 'Questo è il corpo del messaggio.'
    # Invia l'email
send_email(sender_email, sender_password, recipient_email, subject, message, attachments)
print('ok')




