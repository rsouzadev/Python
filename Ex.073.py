from time import sleep
while True:
    n = int(input('Digite um número:'))

    if n > 10:
        print('\033[41mEu só aceito números até 10 ok?\033[m')
    else:
        print(f'Você digitou {n}. Obrigado!')

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer tentar novamente? [S/N]')).strip().upper()[0]

    if escolha in 'S':
        print('OK, vamos lá então!')
        sleep(2)
    else:
        print('Obrigado, volte sempre...')
        break


