import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviarEmail(user_mail, password, receiver_mail, html):
    # Server info
    smtp_server = 'mail.sampaio-sa.com.br'
    port = 465

    # Mail info
    mail = MIMEMultipart('alternative')
    mail['Subject'] = 'Teste'
    mail['From'] = user_mail
    mail['To'] = receiver_mail
    mail.attach(
        MIMEText(html, 'html')
    )

    # Context
    context = ssl.create_default_context()

    # Create server and send email
    with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
        server.login(user_mail, password)
        server.sendmail(user_mail, mail['To'], mail.as_string())