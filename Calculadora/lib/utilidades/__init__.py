def linha(n = 44):
    return '-' * n

def menu(txt):
    print(linha())
    print(txt.center(44))
    print(linha())

def numInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('Valor informado inválido. Digite novamente!')
            continue
        except(KeyboardInterrupt):
            print('\nO campo será preenchido com 0')
            return 0
        else:
            return n

def opcoes(lista):
    menu('OPERAÇÕES')
    c = 1
    for item in lista:
        print(f'{c} -- {item}')
        c += 1
    print(linha())
    opc = numInt('Escolha uma das opções: ')
    return opc

def calculo(opc_usuario, n1, n2):
    while True:
        if opc_usuario == 1:
            return f'A soma de {n1} + {n2} é {n1 + n2}'
        elif opc_usuario == 2:
            return f'A subtração de {n1} - {n2} é {n1 - n2}'
        elif opc_usuario == 3:
            return f'A multiplicação de {n1} * {n2} é {n1 * n2}'
        elif opc_usuario == 4:
            return f'A divisão entre {n1} e {n2} é {n1 / n2}'
        else:
            return 'Infelizmente não temos essa opção!'
        
