import os
from time import sleep


lista = []
print('Bem vindo a sua lista!')
print('-' * 33)
while True:
        print('Escolha uma das opções: ')
        entrada = input('[i]nserir [a]pagar [l]istar [s]air: ').strip()
        opcao = entrada.lower()
#adicionando itens        
        if opcao == 'i':
            os.system('cls')
            adicionar_lista = input('Digite o que quer adicionar: ')
            lista.append(adicionar_lista)
#apagando itens
        elif opcao == 'a':
            os.system('cls')
            for indice, nome in enumerate(lista):
                print(indice, nome)
            apagar_lista= input('Qual indice da lista você deseja apagar? ')
            
            try:
                apagar_lista_int = int(apagar_lista)
                del lista[apagar_lista_int]
                print('Item removido com sucesso!')
            except ValueError:
                print('Por favor, digite um número válido!')
            except IndexError:
                print('Por favor, informe um indice que esteja dentro da lista')            
#listando itens
        elif opcao == 'l':
            os.system('cls')
            
            if len(lista) == 0:
                print('Lista vazia')
            for indice, nome in enumerate(lista):
                print(indice, nome)
            
        elif opcao == 's':
            print('Lista final: ')
            for nome in lista:
                print(nome)
            sleep(10)
            break
        else:
            print('Opção inválida')
