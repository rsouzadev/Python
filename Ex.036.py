print('=====DESAFIO 036=====')
from time import sleep
nome = str(input('Informe o seu nome por favor:'))
print('Olá {}! Seja Bem-vindo!'.format(nome))

vcasa = float(input('Informe o valor da casa que deseja financiar:R$'))
sal = float(input('Informe o seu salário por favor:R$'))
anos = int(input('{}, quantos anos você deseja financiar a sua casa? '.format(nome)))
prestação = vcasa / (anos * 12)
mínimo = sal * 30 /100
print('Calculando...')
sleep(3)
print('Para pagar uma casa de R${:.2f} em {} anos, o valor da prestação será de R${:.2f}'.format(vcasa, anos, prestação))
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO!')

else:
    print('Empréstimo NEGADO!')
