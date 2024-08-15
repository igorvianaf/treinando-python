import os


tentativas = 0
while True: 
    #solicitando cpf e usando replace para retirar . - e espaços
    try:
        cpf_entrada = input('Digite um CPF válido: ')
        cpf_usuario = cpf_entrada.replace('.', '').replace('-', '')
        
        caractere_repetido = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
        if caractere_repetido == True:
            print('Dados sequenciais não são considerados como um CPF válido')
            print('Tente novamente!')
            continue

        #armazenando os 9 primeiros digitos para calculo CPF
        nove_digitos = cpf_usuario[:9]
        #verificador para a quantidade de vezes que o cpf será iterado
        verificador_1 = 10
        #armazenar o valor de cada soma
        soma_dig_1 = 0
        
        #armazenar apenas 11 números no cpf_usuario    
        if len(cpf_usuario) != 11:
            print('Quantidade de digito inválida!')
            print('Por favor, informe um cpf válido!')
            continue

        #iterando para realizar soma e multiplicacao
        for indice in nove_digitos:
            soma_dig_1 += int(indice) * verificador_1
            verificador_1 -= 1

        conta_1 = (soma_dig_1 * 10) % 11
        #condição caso o primeiro digito do cpf seja maior que 10
        primeiro_dig = conta_1 if conta_1 <= 9 else 0


        #descobrindo o segundo digito
        dez_digitos = nove_digitos + str(primeiro_dig)
        verificador_2 = 11
        soma_dig_2 = 0

        for i in dez_digitos:
            soma_dig_2 += int(i) * verificador_2
            verificador_2 -= 1

        conta_2 = (soma_dig_2 * 10) % 11
        segundo_dig = conta_2 if conta_2 <= 9 else 0

        #armazenar o cálculo do cpf
        calculo_cpf = (f'{nove_digitos}{primeiro_dig}{segundo_dig}')
        
        #condição para comparar o cálculo do cpf com o cpf informado pelo usuário
        if cpf_usuario == calculo_cpf:
            os.system('cls')
            print(f'O CPF: {cpf_usuario} é válido')
            print('-' * 10, 'Bem vindo', '-' * 10)
            break
        else:
            print('CPF inválido')

        tentativas += 1 

        #quantidade de vezes para conseguir colocar um cpf válido   
        if tentativas == 4 :
            os.system('cls')
            print('Você atingiu o número máximo de tentativas!')
            print('-' * 15 ,'Acesso negado!', '-' * 15)
            break
    except(ValueError, TypeError):
        print('Não é permitido a utilização de letras em cpf')