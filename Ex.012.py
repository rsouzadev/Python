print('=====DESAFIO 12=====')
print('-'*46)
l = float(input('Informe a largura da sua parede por favor:'))
a = float(input('Informe a altura da sua parede por favor:'))
ar = l * a
li = ar / 2
print('Sua parede possui dimensão de {}x{} e sua área é de {}m2'.format(l,a,ar))
#print('O espaço possui {}m2.'.format(ar))
print('Você precisará de {:.3} litros de tinta para pintar sua casa.'.format(li))
print('-'*46)