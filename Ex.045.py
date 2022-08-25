from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Sua opções:')
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogada = int(input('Qual é a sua jogada?'))
print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)

print('Você jogou {}!'.format(itens[jogada]))
print('O computador jogou {}!'.format(itens[computador]))

print('-='*15)

if jogada == 0 and computador == 1:
    print('Você perdeu!!!')
elif jogada == 0 and computador == 2:
    print('Você ganhou!!!')
elif jogada == 1 and computador == 0:
    print('Você ganhou!!!')
elif jogada == 1 and computador == 2:
    print('Você perdeu!!! ')
elif jogada == 2 and computador == 0:
    print('Você perdeu!')
elif jogada == 2 and computador == 1:
    print('Você ganhou!!!')
else:
    print('Deu empate!')


