import math
print('=====DESAFIO 18=====')
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = math.hypot(co,ca)
#h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))

#hipotenusa raiz quadrada da soma dos quadrados dos catetos.



