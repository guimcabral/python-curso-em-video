# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

var = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(var))
print('Só tem espaços?', var.isspace())
print('É um número?', var.isnumeric())
print('É alfabético?', var.isalpha())
print('É alfanumérico?', var.isalnum())
print('Está em maiúsculas?', var.isupper())
print('Está em minúsculas?', var.islower())
print('Está capitalizada?', var.istitle())
