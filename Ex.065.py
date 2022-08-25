soma = 0
contador = 0
média = 0
resposta = ''
while resposta in 'Ss':
    número = int(input('Digite um número:'))
    soma = soma + número
    contador = contador + 1
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
média = soma / contador
print('Você digitou {} números e a média foi {}'.format(contador,média))