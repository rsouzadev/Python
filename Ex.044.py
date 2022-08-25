print('{:=^50}'.format(' LOJAS GUANABARA ' ))

valor = float(input('Digite o valor da compra: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro /cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3X ou mais no cartão''')
opção = int(input('Qual será a forma de pagamento?'))
if opção == 1:
    total = valor - (valor * 10 / 100)
elif opção == 2:
    total = valor - (valor * 5 / 100)
elif opção == 3:
    total = valor
    parcela = valor / 2
    print('Sua compra de R${:.2f} terá duas parcelas de R${:.2f} SEM JUROS com vencimento no dia 5 de cada mês.'.format(valor, parcela))
elif opção == 4:
    total = valor + (valor * 20 / 100)
    parcelas = int(input('Informe a quantidade de parcelas:'))
    totalparc = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, totalparc))
else:
    total = valor
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f}, vai custar R${:.2f} no final.'.format(valor, total))
