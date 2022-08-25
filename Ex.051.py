print('='*50)
print('{:^50}'.format('10 TERMOS DE UMA PA'))
print('='*50)
ptermo = int(input('Digite o primeiro termo:'))
razão = int(input('Razão:'))
dtermo = ptermo + (10 - 1) * razão
for c in range (ptermo, dtermo + razão, razão):
    print('{}'.format(c), end='→ ')
print('ACABOU!')