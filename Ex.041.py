from datetime import date
ano = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: JÚNIOR')
elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: SÊNIOR')
elif idade > 25:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO:MASTER')

