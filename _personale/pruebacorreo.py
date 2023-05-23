import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename

# Establecer conexión con el servidor SMTP
smtp = smtplib.SMTP('smtp.office365.com', port=587)
smtp.starttls()

# Ingresar credenciales de acceso
smtp.login('holatu2u2@outlook.com', 'holatu1111')

# Crear el mensaje
msg = MIMEMultipart()
msg['From'] = 'holatu2u2@outlook.com'
msg['To'] = 'holatu2u2@outlook.com'
msg['Subject'] = 'Correo con archivo Excel adjunto'

# Agregar texto al mensaje
body = 'Este es un mensaje de prueba'
msg.attach(MIMEText(body, 'plain'))

# Adjuntar el archivo Excel al mensaje
with open('Cartel1.xlsx', 'rb') as f:
    nombre_archivo = basename(f.name)
    archivo = MIMEApplication(f.read(), _subtype='xlsx')
    archivo.add_header('content-disposition', 'attachment', filename=nombre_archivo)
    msg.attach(archivo)

# Enviar el mensaje
smtp.send_message(msg)

# Cerrar la conexión con el servidor SMTP
smtp.quit()
