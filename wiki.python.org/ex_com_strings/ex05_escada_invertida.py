nome = input('Informe o nome: ')
armazenamento1 = ''
armazenamento2 = ''
for letra in nome:
    armazenamento1 += letra
for i in range(len(nome)):
    armazenamento2 = armazenamento1[0:len(nome) -i:]
    print(armazenamento2)