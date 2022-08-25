maior_peso = 0
menor_peso = 0
for c in range(1, 6):
    peso_atual = float(input('Qual é o peso da {}ª pessoa?'.format(c)))
    if c == 1:
        maior_peso = peso_atual
        menor_peso = peso_atual
    else:
        if peso_atual > maior_peso:
            maior_peso = peso_atual
        if peso_atual < menor_peso:
            menor_peso = peso_atual
print('O maior peso lido foi de {}'.format(maior_peso))
print('O menor peso lido foi de {}'.format(menor_peso))