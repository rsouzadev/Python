print('=====DESAFIO 030=====')
n = int(input('Digite um número:'))
resto = n % 2
if resto == 0:
    print('O número {} é um número par!'.format(n))
else:
    print('o número {} é um número ímpar!'.format(n))