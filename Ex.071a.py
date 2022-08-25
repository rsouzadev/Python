import math
titulo = 'BANCO CEV'
print('='*30)
print(titulo.center(30))
print('='*30)
valor = float(input('Digite o valor a ser sacado:R$'))

n100 = valor / 100
r100 = valor % 100
n50 = r100 / 50
r50 = r100 % 50
n20 = r50 / 20
r20 = r50 % 20
n10 = r20 / 10
r10 = r20 % 10
n5 = r10 / 5
r5 = r10 % 5
n1 = r5 / 1

print(f'\n{math.trunc(n100)} notas de R$ 100,00')
print(f'{math.trunc(n50)} notas de R$ 50,00')
print(f'{math.trunc(n20)} notas de R$ 20,00')
print(f'{math.trunc(n10)} notas de R$ 10,00')
print(f'{math.trunc(n5)} notas de R$ 5,00')
print(f'{n1:.0f} notas de R$ 1,00')