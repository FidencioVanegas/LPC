import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username=input("Correo: ")
password=getpass.getpass("Contraseña: ")
destinatario=input("Destinatario: ")
asunto=input("Asunto: ")

mensaje = MIMEMultipart()
mensaje["Subject"]=asunto
mensaje["From"]=username
mensaje["To"]=destinatario

msg="""
Protocolo simple de transferencia de correo (SMTP)
El protocolo simple de transferencia de correo (SMTP) es un protocolo TCP/IP que se utiliza para enviar y recibir correo electrónico.
Normalmente se utiliza con POP3 o con el protocolo de acceso a mensajes de Internet (IMAP) para guardar mensajes en un buzón del servidor y descargarlos periódicamente del servidor para el usuario.

Referencia: https://www.ibm.com/docs/es/i/7.3?topic=information-smtp
"""

message=MIMEText(msg)
mensaje.attach(message)
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(username,password)
    print("Inicio sesion")
    server.sendmail(username,destinatario,mensaje.as_string())
    print("mensaje enviado")
