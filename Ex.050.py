total = 0
contador = 0
for c in range(1, 7):
    n = int(input('Digite o primeiro número:'))
    if n % 2 == 0:
        total = total + n
    elif n % 2 == 1:
        contador = contador + 1
print('Você informou {} ímpares e o total dos pares foi {}:'.format(contador, total))