print('===DESAFIO 038=====')

num1 = int(input('Primeiro número:'))
num2 = int(input('Segundo número:'))
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num1 == num2:
    print('Os dois números são iguais!')
else:
    print('{} é menor que {}'.format(num1, num2))
