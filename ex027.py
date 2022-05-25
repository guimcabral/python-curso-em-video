# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nome_list = nome.split()

print('Seu primeiro nome é {}.'.format(nome_list[0]))
print('Seu último nome é {}.'.format(nome_list[len(nome_list)-1]))
