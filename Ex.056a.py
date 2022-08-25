somaidades = 0
médiadogrupo = 0
homemmaisvelho = 0
totmenos20anos = 0
nomehomemmaisvelho = ''
for p in range(1,5):
    print('-----{}ª PESSOA -----'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidades = somaidades + idade
    if p == 1 and sexo in 'Mm':
        homemmaisvelho = idade
        nomehomemmaisvelho = nome
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomehomemmaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmenos20anos = totmenos20anos + 1
médiadogrupo = somaidades / 4
print('A média de idade do grupo é de {} anos'.format(médiadogrupo))
print('O homem mais velho tem {} anos e se chama {}'.format(homemmaisvelho, nomehomemmaisvelho))
print('Ao todo são {} mulheres com menos de  20 anos'.format(totmenos20anos))
