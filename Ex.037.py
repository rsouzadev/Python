num = int(input('Digite um número por favor:'))
print('''Escolha uma das opções para conversão:
[ \033[33m1\033[m ] Converter para BINÁRIO.
[ \033[31m2\033[m ] Converter para OCTAL.
[ \033[32m3\033[m ] Converter para HEXADECIMAL.
''')
opção = int(input('Sua opção:'))

if opção == 1:
    print('{} convertido para BINÁRIO é igual à: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido em OCTAL é igual à: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é igual à {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')


