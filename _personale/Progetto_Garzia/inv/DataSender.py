import pandas as pd
import os
import shutil
import base64
from email import encoders
import warnings
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import zipfile


class DataSender:
    def __init__(self):
        warnings.simplefilter("ignore")

    @staticmethod
    def send_data():
        data_invio = input('Inserire la (dd/mm/yyyy) data dei lavori che si desiderano inviare: ')
        date = datetime.strptime(data_invio, "%d/%m/%Y").date()
        if not date:
            print('inserire una data valida')
            return

        file_path = "C:/Users/Utente/Documents/Progetto_Garzia/ACE10001I C-Lab HR/DB C-Lab (HRR).xlsx"
        new_file_path = "C:/Users/Utente/Documents/Progetto_Garzia/ACE10001I C-Lab HR/DB C-Lab_(Transfer).xlsx"

        foglio_candidati = DataSender.read_excel_sheet(file_path, 'Candidati')
        posizione_data = foglio_candidati[foglio_candidati.eq(data_invio).any(axis=1)]
        righe_da_copiare = foglio_candidati.loc[posizione_data.index]
        righe_da_copiare.to_excel(new_file_path, index=False, sheet_name='Candidati', engine='openpyxl')

        foglio_anagskill = DataSender.read_excel_sheet(file_path, 'AnagSkill')
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
                    if cognome_nome not in nomi_curriculum:
                        nomi_curriculum.append(cognome_nome)
                        percorsi_cv.append(percorso_cv)
                    print(nomi_curriculum)

        with pd.ExcelWriter(new_file_path, engine='openpyxl', mode='a') as writer:
            anagskill_transfer.transpose().to_excel(writer, index=False, sheet_name='AnagSkill')

        percorso_destinazione = "C:/Users/Utente/Documents/Progetto_Garzia/ACE10001I C-Lab HR/Cartella_Destinazione/"
        for percorso_cv in percorsi_cv:
            percorso_cv_destinazione = os.path.join(percorso_destinazione, os.path.basename(percorso_cv))
            shutil.copy(percorso_cv, percorso_cv_destinazione)

        new_file_path_destinazione = os.path.join(percorso_destinazione, os.path.basename(new_file_path))
        shutil.copy(new_file_path, new_file_path_destinazione)

        percorso_destinazione = "C:/Users/Utente/Documents/Progetto_Garzia/ACE10001I C-Lab HR/Cartella_Destinazione/"
        nome_file_zip = "Cartella_Destinazione.zip"

        with zipfile.ZipFile(nome_file_zip, "w") as zipf:
            for root, dirs, files in os.walk(percorso_destinazione):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, percorso_destinazione)
                    zipf.write(file_path, arcname=relative_path)

        print("La directory è stata zippata correttamente.")

        DataSender.send_email(nomi_curriculum, new_file_path_destinazione)

    @staticmethod
    def read_excel_sheet(file_path, sheet_name):
        return pd.read_excel(file_path, sheet_name=sheet_name)

    @staticmethod
    def send_email(nomi_curriculum, new_file_path_destinazione):
        smtp_server = 'smtp.libero.it'
        smtp_port = 587
        sender_email = 'indirizzohrr@libero.it'
        sender_password = 'indHRR23+'
        receiver_email = 'sedecentrale_2023@libero.it'
        subject = 'Candidati'
        body = """Alla cortese attenzione della Sede Centrale,
        in allegato i file relativi ai candidati selezionati per le richieste ricevute.

        Cordiali saluti"""

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        def attach_file(filename):
            with open(filename, 'rb') as file:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(file.read())
                file_name = os.path.basename(filename)
                attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
                encoders.encode_base64(attachment)
                message.attach(attachment)

        attach_file('C:/Users/Utente/Documents/Progetto_Garzia/Cartella_Destinazione.zip')

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Mail inviata con successo!")
        except Exception as e:
            print("Si è verificato un errore durante l'invio della mail:", str(e))
        finally:
            server.quit()