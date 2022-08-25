print('-' * 30)
print('{:^30}'.format('CADASTRE UMA PESSOA'))
print('-' * 30)
total_m18 = 0
homem = 0
total_m20 = 0
while True:
    idade = int(input('Idade:'))
    escolha = ' '

    sexo = ' '
    while not sexo in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('-' * 30)

    if idade >= 18:
        total_m18 = total_m18 + 1
    if sexo == 'M':
        homem = homem + 1
    elif sexo == 'F' and idade <= 20:
        total_m20 = total_m20 + 1

    while not escolha in 'SN':
        escolha= str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total_m18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {total_m20} mulheres com menos de 20 anos.')

