# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

from time import sleep
from random import randint

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar.')
print('-=-' * 20)

n_pc = randint(0, 5)
n_user = int(input('Em que número eu pensei? '))

print('Processando...')
sleep(2)

if n_user == n_pc:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {}!'.format(n_pc))
