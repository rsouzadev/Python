contador = 0
maior_idade = 0
menor_idade = 0
while contador <= 3:
    nome = str(input('Digite seu nome:'))
    idade = int(input('Digite sua idade:'))
    contador = contador + 1
    if contador == 1:
        maior_idade = menor_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade

print('A maior idade digitada foi {}.'.format(maior_idade))
print('A menor idade registrada foi {}.'.format(menor_idade))