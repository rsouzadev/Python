#from time import sleep
from random import randint

contador = 0
while True:
    num_jogador = int(input('Digite um número por favor:'))
    computador = randint(0, 10)
    total = num_jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {num_jogador} e o computador jogou {computador}. TOTAL = {total}.', end='')
    print(' Deu PAR!' if total % 2 == 0 else ' Deu ÍMPAR!')
    #sleep(1)

    if total % 2 == 0:
        if escolha == 'P':
            print('Você VENCEU!')
            contador = contador + 1
        else:
            print('Você PERDEU!')
            break
    elif total % 2 == 1:
        if escolha == 'I':
            print('Você VENCEU!')
            contador = contador + 1
        else:
            print('Você PERDEU!')
            break

    print('Vamos jogar novamente!')
print(f'GAME OVER BUDDY! Você venceu {contador} vezes!')









