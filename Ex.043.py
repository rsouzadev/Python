peso = float(input('Qual é o seu peso?(Kg)'))
altura = float(input('Qual é a sual altura?(m)'))
imc = peso / (altura * altura)
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal.')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('OBESIDADE MÓRBIDA!')

