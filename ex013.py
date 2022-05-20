# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n = float(input('Qual é o salário do funcionário?\nR$ '))
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a ganhar R$ {:.2f}.'.format(n, n * 1.15))
