lista = list()
while True:
    n = int(input("Digite um valor:"))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Número não adicionado!")

    escolha = str(input("Deseja continuar?[S/N]")).strip().upper()
    if escolha in "Nn":
        break
lista.sort()
print(f'Os valores digitados foram: {lista}.')
