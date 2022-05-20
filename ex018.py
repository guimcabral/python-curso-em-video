# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import tan, cos, sin, radians

ang = radians(float(input('Digite o ângulo, em graus, que você deseja: ')))
print('O ângulo de {:.2f} tem o SENO de {:.2f}.'.format(ang, sin(ang)))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}.'.format(ang, cos(ang)))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}.'.format(ang, tan(ang)))
