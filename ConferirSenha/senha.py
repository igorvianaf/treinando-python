import os

print('Vamos criar sua senha!')
print('A senha precisa ter ao menos 10 caracteres, incluindo números e letras maiúsculas e minúsculas e não pode conter espaço')

while True:
    senha = input('Digite sua senha: ')
    
    cont_minusc = 0
    cont_maiusc = 0
    cont_num = 0
    cont_espaco = 0

    for i in senha:
        if i.isupper():
            cont_maiusc += 1
    for a in senha:        
        if a.islower():
            cont_minusc += 1
    for b in senha:
        if b.isdecimal():
            cont_num += 1
    for c in senha:
        if c.isspace():
            cont_espaco += 1

    erro = []
    if len(senha) < 10:
        erro.append('A senha precisa ter ao menos 10 caracteres.')
    if cont_maiusc == 0:
        erro.append('A senha precisa ter ao menos uma letra maiúscula.')
    if cont_minusc == 0:
        erro.append('A senha precisa ter ao menos uma letra minúscula.')
    if cont_num == 0:
        erro.append('A senha precisa ter ao menos um número.')
    if cont_espaco >= 1:
        erro.append('A senha não pode conter espaços.')


    if erro:
        for mensagem in erro:
            print(mensagem)
    else:
        os.system('cls')
        print('Sua senha passou pelos padrões de segurança. Senha criada com sucesso')
        break
