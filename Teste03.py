print('=====TESTE 03=====')
frase = ('Curso em Video Python')

#print(frase[9::3])
print(len(frase)) #Exibe o número de caracteres
print(frase.count('o')) #count
print(frase.count('o',0,13))#count com fatiamento
print(frase.find('deo'))
print(frase.find('Android'))#não achou
print('Curso'in frase)#tem curso em frase, sim então true
print(frase.replace('Python','Android'))
print(frase.upper())
print((frase.lower()))
print(frase.capitalize())
print(frase.title())#Faz o capitalize palavra por palavra
print(frase.strip()) #remove espaços innuteis menos espaços do meio
print(frase.rstrip())#remove os espaços da direita
print(frase.lstrip())#remove os espaços da esquerda
print(frase.split())# divide palavra por palavra em lista
print('-'.join(frase))
dividido = frase.split()
print(dividido[0][2])
print(dividido[2])


