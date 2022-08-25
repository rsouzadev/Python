n = 0
soma = 0
contador = 0
while n != 999:
    n = int(input('Digite um valor: [999 para parar]'))
    if n == 999:
        break
    soma = soma + n
    contador = contador + 1
print('A soma dos {} valores é {}.'.format(contador,soma),)
print(f'A soma dos {contador} valores é {soma}.')