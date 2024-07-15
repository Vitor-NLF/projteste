print("Dê as medidas de  um triângulo, logo abaixo!")
A = float(input("Digite o primeiro valor: "))
B = float(input("Digite o segundo valor: "))
C = float(input("Digite o terceiro valor: "))

if(A == B == C):
    print("O triângulo é equilátero!!")
elif(A == B) and (A,B != C):
    print("O triângulo é isósceles!!")
elif(A != B != C):
    print("O triângulo é escaleno!!")