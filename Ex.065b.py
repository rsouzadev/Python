menortemperatura = 0
maiortemperatura = 0
for c in range(0,4,1):
    temperatura = int(input('Temperatura em SP:'))
    if temperatura > maiortemperatura:
        maiortemperatura = temperatura
    if temperatura < menortemperatura:
        menortemperatura = temperatura
print('A maior temperatura registrada em São Paulo foi {}.'.format(maiortemperatura))
print('A menor temperatura foi {}.'.format(menortemperatura))
