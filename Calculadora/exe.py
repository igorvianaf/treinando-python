from lib.utilidades import menu, numInt, opcoes, calculo
import os


while True:
    menu('CALCULADORA')
    n1 = numInt('Digite o primeiro valor: ')
    n2 = numInt('Digite o segundo valor: ')
    entrada_usuario = opcoes(['Somar', 'Subtrair', 'Multiplicar', 'Dividir'])
    print(calculo(entrada_usuario, n1, n2))

    flag = True
    while flag:
        sair = input('Gostaria de realizar uma nova operação? [S/N]: ')[0].upper().strip()
        if sair in 'S':
            os.system('cls')
            flag = False
        elif sair in 'N':
            os.system('cls')
            print('Até logo, espero que você retorne em breve!')
            flag = False
        else:
            print('O campo só recebe [S - Sim/ N - Não]')
    if flag == False:
        break
