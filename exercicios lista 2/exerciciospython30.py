a = float(input("Digite o valor: "))
b = input("Digite a sigla do estado distinto: ")

if(b == "MG"):
    a1 = 0.7 * a
    print(a1)
elif(b == "SP"):
    a2 = 0.12 * a
    print(a2)
elif(b == "RJ"):
    a3 = 0.15 * a
    print(a3)
elif(b == "MS"):
    a4 = 0.8 * a
    print(a4)