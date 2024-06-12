import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def enviar(email, nombre, fecha, hora, materia):
    
    user = st.secrets["emails"]["smtp_user"]
    password = st.secrets["emails"]["smtp_password"]
    sender_email = "SUDOKU"
    msg = MIMEMultipart()
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = "Reserva de pasantia - SUDOKU"

    message = f"""
    Hola {nombre}
    Su reserva ha sido realizada con éxito.
    Fecha: {fecha}
    Hora: {hora}
    Materia: {materia}

    Gracias por confiar en nosotros - SUDOKU
    """

    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(user, password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        
    except smtplib.SMTPException as e:
        st.exception("Error al enviar el email")