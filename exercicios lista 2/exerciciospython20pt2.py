n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

P1 = 1
P2 = 1
P3 = 2
Pf = P1 + P2 + P3

R = (n1 + n2) * 1
R2 = (n3) * 2
R3 = (R + R2) / Pf
R4 = R3 * 10

print("A nota é: ",R4)
if(R4 > 60):
    print("Você está aprovado(a)!!!")
elif(R4 < 60):
    print("Você não está aprovado(a)!!!")    