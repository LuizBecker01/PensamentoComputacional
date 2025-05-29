import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(padrao, email))

#testes
emails = ['usuario@gmail.com', 'usuario2@gmail.com','usuario3@Gmail.com', 'aaa0.gmailcom']

for email in emails:
    print(f'{email}: {'é válido' if validar_email(email) else "não é válido"}')
    
