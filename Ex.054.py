from datetime import date
data_atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8, ):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?'.format(pess)))
    idade = data_atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))


    

