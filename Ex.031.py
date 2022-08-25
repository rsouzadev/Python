print('=====DESAFIO 031=====')

d = float(input('Informe a distância da sua viagem por favor:'))
p1 = d * 0.50
p2 = d * 0.45
if d <= 200:
    print('Sua viagem de {:.2f} kms custará R$ {}'.format(d, p1))
else:
    print('Sua viagem de {:.2f} kms custará R$ {}'.format(d,p2))

