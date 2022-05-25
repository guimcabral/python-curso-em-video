# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distância da sua viagem? '))
if dist > 200:
    preco = dist * 0.45
else:
    preco = dist * 0.5

# ou preco = dist * 0.45 if dist > 200 else dist * 0.5
print('A viagem de {:.2f}km custará R$ {:.2f}.'.format(dist, preco))
