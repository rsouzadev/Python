print('-'*50)
print('{:^50}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-'*50)

termos = int(input('Quantos termos você quer mostrar?'))

t1 = 0
t2 = 1
print('{}→{}'.format(t1,t2),end='')

contador = 3
while contador <= termos:
    contador = contador + 1
    t3 = t1 + t2
    print('→{}'.format(t3),end='')
    t1 = t2
    t2 = t3
print('FIM')

