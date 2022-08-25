from random import randint
contador = 0
while True:
    jogador = int(input('Digite um número:'))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            contador = contador + 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif escolha == 'I':
        print('Você VENCEU!')
        contador = contador + 1
    else:
        print('Você PERDEU!')
        break
    print(f'Você jogou {jogador} e eu joguei {computador}. Total de {total}. ', end='')
    print('Deu PAR!' if total % 2 == 0 else 'Deu ÍMPAR!')
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {contador} vezes.')



