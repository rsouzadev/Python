print('=====DESAFIO 023=====')
nome = str(input('Qual é o seu nome?')).strip() #remove os espaços nos lados.
print('O seu nome com as letras maiúsculas fica assim: {}'.format(nome.upper()))
print('O seu nome com as letras minúsculas fica assim meu rei: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #mostra quantos caracteres tem menos a contagem dos espaços do meio das palavras.
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
#print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))