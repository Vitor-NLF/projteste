a = float(input("Digite a distância em Km: "))
b = float(input("Digite a quantidade de litros consumido: "))

c = a/b
print(c)
if(c <= 8):
    print("VENDA O CARRO!")
if(c >= 8) and (c <= 14):
    print("ECONÔMINCO!")
if (c >= 12):
    print("SUPER ECONÔMICO!")