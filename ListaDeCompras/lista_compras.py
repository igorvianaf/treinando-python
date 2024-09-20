import os
import json
from time import sleep


def adicionar(item):
    lista.append(item)
    print(f'{item} foi adicionado a sua lista!')
    if lista_desfazer:
        lista_desfazer.pop()

def exibir(lista):
    if not lista:
        print('Lista vazia!')
        return
    for indice, nome in enumerate(lista):
        print(indice, nome)

def apagar_item(item, lista):
    if not lista:
        print('Não temos itens para apagar em sua lista')
        return
    try:
        apagar_lista_int = int(item)
        print(f'{lista[apagar_lista_int]} foi removido com sucesso!')
        lista_desfazer.append(lista[apagar_lista_int])
        del lista[apagar_lista_int]

    except ValueError:
        print('Por favor, digite um número válido!')
    except IndexError:
        print('Por favor, informe um indice que esteja dentro da sua lista')

def desfazer_alteracao(lista, desfazer_alteracao):
    if not lista:
        print('No momento, sua lista está vazia!')
        return
    if desfazer_alteracao:
        ultimo_apagado = desfazer_alteracao[-1]
        lista.append(ultimo_apagado)
        print(f'A alteração foi desfeita com sucesso')
        print(f'{ultimo_apagado} foi restaurado!')
        desfazer_alteracao.pop()
    elif lista:    
        ultimo_excluido = lista.pop()
        desfazer_alteracao.append(ultimo_excluido)
        print(f'A alteração foi desfeita com sucesso')
        print(f'{ultimo_excluido} foi excluído!')

def limpar_tela():
    os.system('cls')

def ler_arquivo(lista, caminho_arquivo):
    try:
        dados = []
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        salvar_novo_arquivo(lista, caminho_arquivo)

def salvar_novo_arquivo(lista, caminho_arquivo):
    dados = lista
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(lista, arquivo, indent=2, ensure_ascii=False)
    return dados

def verificar_opcoes(entrada_usuario):
#Adicionar itens
    if entrada_usuario == 'i':
        limpar_tela()
        adicionar(input('Informe o que deseja adicionar: '))
#apagando itens
    elif entrada_usuario == 'a':
        limpar_tela()
        exibir(lista)
        apagar_item(input('Qual índice da lista você deseja apagar? '), lista)
#listando itens
    elif entrada_usuario == 'l':
        limpar_tela()
        exibir(lista)
#desfazer alteração
    elif entrada_usuario == 'd':
        desfazer_alteracao(lista, lista_desfazer)
#sair
    elif entrada_usuario == 's':
        print('Lista final: ')
        exibir(lista)
        sleep(10)
        return False
    else:
        print('Opção inválida')


CAMINHO_ARQUIVO = 'C:\\Users\\igorv\\OneDrive\\Documentos\\GitHub\\treinando-python\\ListaDeCompras\\lista.json'
lista = ler_arquivo([], CAMINHO_ARQUIVO)
lista_desfazer = []

print('Bem vindo a sua lista!')
print('-' * 33)
while True:
        print('Escolha uma das opções: ')
        opcoes = verificar_opcoes(input('[i]nserir [a]pagar [l]istar [d]esfazer última alteração [s]air: '))
        if opcoes == False:
            break
        salvar_novo_arquivo(lista, CAMINHO_ARQUIVO)
