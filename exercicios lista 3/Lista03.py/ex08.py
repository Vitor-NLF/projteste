lista = []
i = 1

while i <= 10:
    numero = int(input("Digite um número: "))
    if numero >= 0:
        lista.append(numero)
        i = i + 1
    elif numero < 0:
        print("Inválido")
        print("Não será inserido na lista!")
media = sum(lista) / len(lista)
print(media)
print(lista)