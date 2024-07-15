lista = []
i = 1
while len (lista) < 10:
    lista.append(int(input("Digite a nota: ")))
    i = i + 1
    media = sum(lista)/len(lista)
print(media)