print('=====DESAFIO 033=====')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O número maior é o {}'.format(maior))
print('O número menor é o {}'.format(menor))

