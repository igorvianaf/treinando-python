def checar_cupom(cupom):
    for chave in cupons.keys():
        if chave in cupom:
            return True
        else:
            return False


cupons = {
    'cupom10': 0.1,
    'cupom20': 0.2,
    'cupom30':0.3
    }


entrada_usuario = input('Digite um cupom válido: ').strip()
checar_cupom(entrada_usuario)
