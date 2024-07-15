import math
x = float(input("Digite o ponto x1: "))
y = float(input("Digite o ponto y1: "))
z = float(input("Digite o ponto x2: "))
a = float(input("Digite o ponto y2: "))
R = math.sqrt ((x - z) **2 + (y - a) **2)
print(f"A distância entre os pontos é: {R}")
if R > 10:
    print("LONGE")
else:
    print("PERTO")    