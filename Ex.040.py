nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média = (nota1 + nota2) / 2
print('Tirando {:.2f} e {:.2f}, sua média é: {}'.format(nota1, nota2, média))
if média >= 6.5:
    print('VOCÊ ESTÁ APROVADO! PARABÉNS!')
elif média == 6.0:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO!')
elif média < 6.0:
    print('INFELIZMENTE VOCÊ ESTÁ REPROVADO!')

