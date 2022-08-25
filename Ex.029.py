print('=====DESAFIO 29=====')
from time import sleep
print('='*50)
speed = float(input('Type your speed:'))
ticket = (speed-80) * 7
print('\033[31mCHECKING...\033[m')
sleep(4)
if speed > 80:
    print('You will get a ticket of USD {:.2f}'.format(ticket))
    print('Speed limit in this area is 80km/h!')
else:
    print('You are fine but watch out for the speed limit!')

print('=' * 50)