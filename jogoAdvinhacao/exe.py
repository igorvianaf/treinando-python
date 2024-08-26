import util
import os
from time import sleep


print('-' * 21,'JOGO DE ADIVINHAÇÃO', '-' * 21)
sleep(2)
print('O jogador 1 informará uma letra e o jogador 2 terá que adivinhar')
sleep(2)
jogador1 = input('--> Jogador 1, Digite seu nome: ').strip()
jogador2 = input('--> Jogador 2, digite seu nome: ').strip()

print(f'{jogador1} agora é sua vez!', end=' ')
lmisteriosa = util.checarLetra(l='')
os.system('cls')
# lmisteriosa = input(f'{jogador1}, digite a letra misteriosa: ')
letras = set()
cont = 0
while True:
    letra = input(f'{jogador2}, qual letra foi digitada por {jogador1}: ')
    if letra.isnumeric() or letra.isspace():
        print('O campo recebe apenas letras')
        continue
    else:
        letras.add(letra)
        cont += 1
    
    if lmisteriosa in letras:
        os.system('cls')
        print(f'Parábens, com {cont} tentativas, você conseguiu descobrir a letra escolhida por {jogador1}')
        break
    else:
        os.system('cls')
        print('Não foi dessa vez!')
        print(f'Letras que já foram testadas: {letras}')
    
    sair = input(f'{jogador2}, você deseja desistir? [S - Sim/ N - Não]: ').upper()
    if sair in 'S':
        print(f'A letra escolhida por {jogador1} foi {lmisteriosa}. Volte sempre!!')
        sleep(3)
        break
    elif sair in 'N':
        print(f'Muito bom, {jogador2}. Vamos tentar novamente!')
        continue
    else:
        print('O campo só recebe S - sim / N - não')