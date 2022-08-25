import math
print('=====DESAFIO 17=====')
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))
# posso fazer sem importar a biblioteca usando o método (int)
# se eu quiser não preciso importar toda a biblioteca, from math import trunc