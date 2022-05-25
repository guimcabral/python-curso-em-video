# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual é a velocidade atual do carro? '))

if vel > 80:
    print('Multado! Você excedeu o limite de 80km/h.')
    print('Você deve pagar uma multa de R$ {:.2f}!'.format(7 * (vel - 80)))

print('Tenha um bom dia! Dirija com segurança!')
