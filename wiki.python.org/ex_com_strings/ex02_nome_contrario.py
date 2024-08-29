nome_contrario = ''
nome = input('Digite seu nome: ')

for letra in nome[::-1]:
    nome_contrario += letra

print(nome_contrario)