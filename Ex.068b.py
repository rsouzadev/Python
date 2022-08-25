while True:
    n1 = int(input('Digite um número:'))
    n2 = int(input('Digite outro:'))
    soma = n1 + n2
    print('A soma de {} + {} é: {}'.format(n1,n2,soma))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'S':
        print('OK!')
    else:
        break
print('JOGO ENCERRADO!')
