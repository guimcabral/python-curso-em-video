# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual é o salário do funcionário? R$ '))

if sal > 1250:
    sal_novo = 1.1 * sal
else:
    sal_novo = 1.15 * sal

print('O salário de R$ {:.2f} passa a ser de R$ {:.2f}.'.format(sal, sal_novo))
