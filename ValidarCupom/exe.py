def checar_cupom(cupom):
    for chave in cupons.keys():
        if chave in cupom:
            return True
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
    'cupom10': 0.1,
    'cupom20': 0.2,
    'cupom30':0.3
    }

while True:
    entrada_usuario = input('Digite um cupom válido: ').strip()
    
    if checar_cupom(entrada_usuario):
        print('Cupom válido')
        break
    else:
        print('Cupom Inválido!')
        flag = sair(input('Deseja adicionar um novo cupom [S - Sim/N - Não]? ').upper())
        if flag:
            continue
        elif flag is False:
            break
        elif flag is None:
            sair(input('Deseja adicionar um novo cupom [S - Sim/N - Não]? ').upper())
