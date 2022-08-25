print('===========PROGRAMA DE ALISTAMENTO EXÉRCITO BRASILEIRO===========')

from datetime import date

nome = str(input('Informe o seu nome por favor:'))
print('Olá {}, seja bem-vindo ao programa de alistamento militar!'.format(nome))
print('''[ 1 ] MASCULINO 
[ 2 ] FEMININO''')
opção = str(input('Escolha uma opção acima:'))
if opção == 1:
    print('Muito bem {}, veja as informações a seguir.'.format(nome))

else:
    print('Você não precisa fazer o seu alistamento!')

nascimento = int(input('Informe o seu ano de nascimento:'))
atual = date.today().year
idade = atual - nascimento
alistamento = (atual - nascimento) - 18
alistamento1 = 18 - idade
print('Quem nasce em {}, tem {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
            print('Chegou a hora do seu alistamento! Corra!')
elif idade > 18:
            print('Já passou {} anos para você se alistar!'.format(alistamento))
            print('Seu alistamento foi em {}.'.format(nascimento + 18))
elif idade < 18:
            print('Ainda faltam {} anos para você se alistar!'.format(alistamento1))
            print('Seu alistamento será em {}'.format(nascimento + alistamento1))





