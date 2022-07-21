import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():
    # Server info
    smtp_server = 'mail.sampaio-sa.com.br'
    port = 465

    # User info
    # user_mail = input('digite o email: ')
    password = input('digite a senha: ')

    # Mail info
    mail = MIMEMultipart('alternative')
    mail['Subject'] = 'Teste'
    mail['From'] = user_mail
    mail['To'] = 'gianluca.ar@sampaio-sa.com.br'
    mail.attach(
        MIMEText('''\
            <html>
                <body>
                    <p>
                        example plain text.
                        <br><br>
                        example plain text.
                    </p>
                <body>
            </html>
            ''',
        'html')
    )

    # Context
    context = ssl.create_default_context()

    # Create server and send email
    with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
        server.login(user_mail, password)
        server.sendmail(user_mail, mail['To'], mail.as_string())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error: %s' % e)
