print('========== PESQUISA ROCK==========' )
totalrock = 0
hmaisvelho = 0
nomehmaisvelho = ''
hmaisnovo = 0
nomehmaisnovo = ''
for p in range(1,4):
    print('{}ª PESSOA'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    rock = str(input('Gosta de Rock [S/N]:')).strip()
    if p == 1 and sexo in 'Mm':
        hmaisvelho = idade
        nomehmaisvelho = nome
        hmaisnovo = idade
        nomehmaisnovo = nome

    if idade > hmaisvelho and sexo in 'Mm':
        hmaisvelho = idade
        nomehmaisvelho = nome
    if idade < hmaisnovo and sexo in 'Mm':
        hmaisnovo = idade
        nomehmaisnovo = nome
    if rock in 'Ss':
        totalrock = totalrock + 1
    

print('Ao total temos {} pessoas que gostam de Rock.'.format(totalrock))
print('O homem mais velho tem {} anos e se chama {}.'.format(hmaisvelho, nomehmaisvelho))
print('O homem mais novo tem {} anos e se chama {}.'.format(hmaisnovo, nomehmaisnovo))