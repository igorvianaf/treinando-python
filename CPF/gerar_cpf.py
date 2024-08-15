import random
from time import sleep


try:
    quantidade_gerar = input('Quantos números de CPF você deseja gerar? ')

    for x in range(int(quantidade_gerar)):
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        #verificador para a quantidade de vezes que o cpf será iterado
        verificador_1 = 10

        #armazenar o valor de cada soma
        soma_dig_1 = 0
            

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
        novo_cpf = (f'{nove_digitos}{primeiro_dig}{segundo_dig}')

        print(novo_cpf)
    #tempo para suspender a execucao do arquivo pelo terminal
    sleep(10)

except(ValueError, TypeError):
    print('O valor informado não é válido')