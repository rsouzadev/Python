print('='*50)
print('{:^50}'.format('TERMOS DE UMA PROGRESSÃO ARITMÉTICA'))
print('='*50)
ptermo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão:'))
termo = ptermo
cont = 1
while cont <= 10:
    print('{} →'.format(termo), end='')
    termo = termo + razão
    cont = cont +1
print('FIM')



