print('='*50)
print('{:^56}'.format('\033[33mGERADOR DE P.A. 3.0\033[m'))
print('='*50)
termo = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
opção = 0
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo,end=' → ')
        termo = termo + razão
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} mostrados.'.format(total))




