sequencia = (int(input('Digite um número:')),
             int(input('Digite outro número:')),
             int(input('Digite mais número:')),
             int(input('Digite o último número:')))
print(f'Você digitou os valores {sequencia}')
print(f'O número 9 apareceu {sequencia.count(9)} vezes.')
if 3 in sequencia:
    print(f'O primeiro número 3 apareceu na posição {sequencia.index(3)+1}.')
else:
    print('O número 3 não foi digitado!')
print('Os números pares foram',end=' ')
for n in sequencia:
    if n % 2 == 0:
        print(n, end='. ')
