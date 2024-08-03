#codigo principal
from lib.utilidades import *

while True:
    menu('CALCULADORA')
    n1 = numInt('Digite o primeiro valor: ')
    n2 = numInt('Digite o segundo valor: ')

    entrada_usuario = opcoes(['Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Sair'])

    if entrada_usuario == 1:
        print(1)
    elif entrada_usuario == 2:
        print(2)
    elif entrada_usuario == 3:
        print(3)
    elif entrada_usuario == 4:
        print(4)
    elif entrada_usuario == 5:
        break
    else:
        print('Infelizmente não temos essa opção. Por favor, tente novamente!')
