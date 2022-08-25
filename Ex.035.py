print('\033[1;31;40m=====DESAFIO 035=====\033[m')
a = float(input('Informe o primeiro lado do triângulo:'))
b = float(input('Informe o segundo lado do triângulo:'))
c = float(input('Informe o terceiro lado do triângulo:'))

if a + b > c and b + c > a and c + a > b:
    print('Os números acima podem formar um triângulo.')
else:
    print('Os números acima não podem formar um triângulo.')
