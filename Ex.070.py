print('-'*40)
print('{:^40}'.format('LOJAS SUPER BARATÃO'))
print('-'*40)

total = 0
tot_mil = 0
menor = 0
cont = 0
while True:
    produto = str(input('Nome do produto:'))
    preço = float(input('Preço: R$'))
    cont = cont + 1
    total = total + preço
    if preço >= 1000:
        tot_mil = tot_mil + 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto


    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
print('-------------FIM DO PROGRAMA-------------')
print(f'O total da compra foi de R$ {total:.2f}.')
print(f'Temos {tot_mil} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}.')

