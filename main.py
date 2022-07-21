import smtplib
import smtplib, ssl


def main():
    # Server info
    smtp_server = 'mail.sampaio-sa.com.br'
    port = 465

    # User info
    user_mail = input('digite o email: ')
    password = input('digite a senha: ')

    # Mail info
    receiver_mail = 'gianluca.ar@sampaio-sa.com.br'
    text = '''\
    example plain text.
    
    example plain text.'''

    # Context
    context = ssl.create_default_context()

    # Create server and send email
    with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
        server.login(user_mail, password)
        server.sendmail(user_mail, receiver_mail, text)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error: %s' % e)
