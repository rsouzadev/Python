print('===FOR===')
for c in range(1,5):
    name = str(input('WHat´s your name?'))
print('===WHILE===')

cont = 1
while cont < 5:
    name = str(input('What´s your name?'))
    cont = cont + 1

cont = 'S'
while cont == 'S':
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('Fim')