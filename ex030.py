# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Me diga um número qualquer: '))

if n % 2 == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))
