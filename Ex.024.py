print('=====DESAFIO 24=====')
num = int(input('Digite um número:'))
print('Analizando meu querido...')
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('A unidade desse número é {}'.format(unidade))
print('A unidade desse número é {}'.format(dezena))
print('A unidade desse número é {}'.format(centena))
print('A unidade desse número é {}'.format(milhar))
