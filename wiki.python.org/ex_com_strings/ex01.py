"""Programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo."""

string1 = input('Informe a frase 1: ').strip().upper()
string2 = input('Informe a frase 2: ').strip().upper()
tamanho_str_1 = len(string1)
tamanho_str_2 = len(string2)

print(f'A 1ª frase possui {tamanho_str_1} caracteres!')
print(f'A 2ª frase possui {tamanho_str_2} caracteres!')

if string2 != string1:
    print('As duas strings possuem conteúdo diferente!')
else:
    print('As duas strings possuem conteúdo igual!')


