def checarLetra(l):
    while True:
        letra = input('Digite uma letra: ')
        if letra.isnumeric() or letra.isspace():
            print('O campo recebe apenas letras')
        else:
            l = letra
            return l