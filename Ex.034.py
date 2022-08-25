print('=====DESAFIO 034=====')
from time import sleep
print('='* 70)
nome = str(input('Informe o seu nome por favor:'))
sal = float(input('Olá {}! Informe o seu salário atual por favor:R$'.format(nome)))
aum1 = sal * (10/100)
aum2 = sal * (15/100)
print('Analizando...')
sleep(3)
if sal > 1250:
    aum1 = sal + aum1
    print('Seu salário sofreu ajuste de \033[0;31m10%, considere R${:.2f}\033[m'.format(aum1))
if sal <= 1250:
    aum2 = sal + aum2
    print('Seu salário sofreu ajuste de \033[0;31m15%, considere R${:.2f}\033[m'. format(aum2))
print('=' * 70)