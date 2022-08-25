soma = 0
média = 0
contador = 0
resposta = ''
nummaior = 0
nummenor = 0
while resposta in 'Ss':
    número = int(input('Digite um número:'))
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    soma = soma + número
    contador = contador + 1
    if contador == 1:
        nummaior = nummenor = número
    else:
        if número > nummaior:
            nummaior = número
        if número < nummenor:
            nummenor = número
média = soma / contador
print('Você digitou {} números e a média foi {:.1f}'.format(contador, média))
print('O maior valor foi {} e o menor foi {}.'.format(nummaior, nummenor))
