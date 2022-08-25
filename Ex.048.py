soma = 0
contador = 0
for c in range (1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        contador = contador + 1
print(' Temos {} números ímpares divisiveis por 3; total {}.'.format(contador, soma))



