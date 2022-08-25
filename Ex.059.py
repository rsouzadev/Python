primeirov = int(input('Primeiro valor:'))
segundov = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Digite sua opção:'))
    if opção == 1:
        soma = primeirov + segundov
        print('A soma entre {} e {} é: {}.'.format(primeirov, segundov, soma))
    elif opção == 2:
        mult = primeirov * segundov
        print('A multiplicação entre {} e {} é: {}'.format(primeirov,segundov,mult))
    elif opção == 3:
        maior = primeirov
        if primeirov > segundov:
            maior = primeirov
        else:
            maior = segundov
        print('Entre {} e {}, o número maior é: {}.'.format(primeirov,segundov, maior))
    elif opção == 4:
        primeirov = int(input('Primeiro valor:'))
        segundov = int(input('Segundo valor:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
print('Fim do programa! Volte sempre!')