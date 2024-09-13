def checar_cupom(cupom):
    for k, v in cupons.items():
        if k in cupom:
            return v
        else:
            return False
def sair(string):
    if string in 'S':
        return True
    elif string in 'N':
        return False
    else:
        print('Por favor, digite uma opção válida!')


cupons = {
    'cupom10': 10,
    'cupom20': 20,
    'cupom30': 30
    }

while True:
    entrada_usuario = input('Digite um cupom válido: ').strip()
    valor = checar_cupom(entrada_usuario)
    if valor:
        print(f'Parabéns! Desconto de {valor}% adicionado!')
        break
    else:
        print('Cupom Inválido!')
        flag = sair(input('Deseja adicionar um novo cupom [S - Sim/N - Não]? ').upper())
        if flag:
            continue
        elif flag is False:
            print('Até logo!')
            break
        elif flag is None:
            sair(input('Deseja adicionar um novo cupom [S - Sim/N - Não]? ').upper())
