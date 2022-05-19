# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a {}cm e {}mm'.format(n, n*100, n*1000))
