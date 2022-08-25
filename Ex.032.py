print('=====DESAFIO 032=====')
from time import sleep
from datetime import date
ano = int(input('Digite o ano que você quer analizar? Coloque 0 para analizar o ano atual:'))
print('Analizando...')
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))

