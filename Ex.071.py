print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
valor = int(input('Digite o valor a ser retirado:R$'))
total = valor
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total = total - céd
        totalcéd = totalcéd + 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédulas de R${céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalcéd = 0
        if total == 0:
            break
print('='*40)
print('Volte sempre ao banco CEV! Tenha um bom dia!')