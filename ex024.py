# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em que cidade você nasceu? ')).strip()
print('A cidade começa com \"Santo\"?', end=' ')
print(cidade.split()[0].lower().__eq__('santo'))  # ou cidade[:5].upper() == 'SANTO'
