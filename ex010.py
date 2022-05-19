# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n = float(input('Quanto dinheiro você tem na carteira?\nR$ '))
dolar = 4.93  # cotação de 19 de maio de 2022 às 20:08 UTC-03:00 (horário de Brasília)
print('Com R$ {:.2f} você pode comprar US$ {:.2f}.'.format(n, n / dolar))
