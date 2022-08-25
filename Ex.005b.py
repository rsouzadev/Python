print('=====DESAFIO EX.005B=====')
a = input('Digite alguma coisa:')
b = input('Digite outra coisa:')
print('O tipo primitivo de {} e {} é:'.format(a, b), type(a))

print('A primeira palavra tem espaços?', a.isspace())
print('A primeira palavra é um número?', a.isnumeric())
print('A segunda palavra é um número?', b.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em letras maiúsculas?', a.isupper())
print('Está em letras minúsculas?', a.islower())
print('Tem letra maiúscula?', a.istitle())








