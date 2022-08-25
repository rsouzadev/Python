
contador = 0
for c in range(1, 5):
    bonito = str(input('Você é bonito?')).strip().upper()
    if bonito == 'SIM':
        contador = contador + 1
print('Você disse sim {} vezes'.format(contador))


