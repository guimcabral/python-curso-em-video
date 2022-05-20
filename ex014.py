# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Informe a temperatua em ºC: '))
fahrenheit = celsius * 9 / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(celsius, fahrenheit))
