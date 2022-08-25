print('BEM-VINDO A MINHA TABUADA')
n = int(input('Digite um número por favor:'))
for c in range(1, 11, ):
    print('{} X {:2} = {}'.format(n, c, n * c))
