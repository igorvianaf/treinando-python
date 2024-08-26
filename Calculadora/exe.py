from lib.utilidades import menu, numInt, opcoes
import os



while True:

    menu('CALCULADORA')
    n1 = numInt('Digite o primeiro valor: ')
    n2 = numInt('Digite o segundo valor: ')

    entrada_usuario = opcoes(['Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Sair'])

    if entrada_usuario == 1:
        print(f'A soma de {n1} + {n2} é {n1 + n2}')
    elif entrada_usuario == 2:
        print(f'A subtração de {n1} - {n2} é {n1 - n2}')
    elif entrada_usuario == 3:
        print(f'A multiplicação de {n1} * {n2} é {n1 * n2}')
    elif entrada_usuario == 4:
        print(f'A divisão entre {n1} e {n2} é {n1 / n2}')
    elif entrada_usuario == 5:
        break
    else:
        print('Infelizmente não temos essa opção!')


    flag = True
    while flag:
        sair = input('Gostaria de realizar uma nova operação? [S/N]: ')[0].upper().strip()
        if sair in 'S':
            os.system('cls')
            break
        elif sair in 'N':
            os.system('cls')
            print('Até logo, espero que você retorne em breve!')
            flag = False
        else:
            print('O campo só recebe [S - Sim/ N - Não]')

    if flag == False:
        break
