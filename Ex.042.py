
a = float(input('Informe o primeiro lado do triângulo:'))
b = float(input('Informe o segundo lado do triângulo:'))
c = float(input('Informe o terceiro lado do triângulo:'))

if a + b > c and b + c > a and c + a > b:
    print('Os números acima podem formar um triângulo ', end='')
    if a == b and b == c and c == a:
        print('EQUILÁTERO')
    elif a != b and b != c and c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os números acima não podem formar um triângulo.')
