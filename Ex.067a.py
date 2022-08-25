print('=' * 50)
n1 = int(input('Quer ver a tabuada de qual valor?'))
print('=' * 50)
contador = 1
#for contador in range(1,11,1):
while contador <= 10:
    multiplicação = n1 * contador
    print('{} x {} = {}'.format(n1, contador, multiplicação))
    contador = contador + 1