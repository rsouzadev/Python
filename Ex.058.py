print('='*80)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10, tente adivinhar...')
from random import randint
computador = randint(0,10)
contador = 0
jogador = int(input('Qual é o seu palpite?'))

if computador == jogador:
    print('Acertou! Parabéns!')
while jogador != computador:
    if jogador > computador:
        print('Menos...')
    if jogador < computador:
        print('Mais...')
    jogador = int(input('Qual é o seu palpite?'))
    if computador == jogador:
        print('Acertou! Parabéns!')
    contador = contador + 1
print('Depois de {} tentativas você acertou!'.format(contador))
print('O número que eu pensei foi {}, Parabéns!'.format(computador))

