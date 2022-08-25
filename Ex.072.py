from time import sleep
n_extenso = ('zero','um','dois','três','quatro','cinco','seis',
             'sete', 'oito','nove','dez','onze','doze','treze',
             'catorze',
             'quinze','dezesseis', 'dezessete','dezoito',
             'dezenove','vinte',)

while True:
    n = int(input('Digite um número entre 0 e 20:'))
    if n < 0 or n > 20:
        print('Tente novamente...')
    else:
        print(f'Você digitou o número {n_extenso[n]}.')
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha == 'S':
        print('OK! Vamos lá então!')
        sleep(2)
    else:
        print('Até + tarde pequeno gafanhoto!')
        break







