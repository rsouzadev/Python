from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),
randint(1,10))
print(f'Os números sorteados foram: {numeros}')
print(f'O maior número sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)} ')
print('====OUTRA FORMA DE SE FAZER USANDO O FOR===')
for c in numeros: #Para cada elemento em números...repetir
    print(f'{c}',end=' ')