
print('=====DESAFIO 028A=====')
print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
from random import randint

computador = randint(0,5)
jogador = int(input('Em que número eu pensei?'))
print('\033[31mPROCESSANDO...\033[m')
sleep(3)

if jogador == computador:
    print('Acertou! Parabéns!')


else:
    print('GANHEI!!! o número que eu pensei foi o {} e não o {}'.format(computador,jogador))
