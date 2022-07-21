from src.enviarEmail import enviarEmail

def main():

    user_mail = input('EMAIL: ') # seu email
    password = input('SENHA: ') # sua senha de login
    receiver_mail = input('DESTINATÁRIO: ') # email do destinatario
    html = '''
        <html>
            <body>
                <p>
                    example plain text.
                    <br><br>
                    example plain text.
                </p>
            <body>
        </html>
        '''

    enviarEmail(user_mail, password, receiver_mail, html)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error: %s' % e)
