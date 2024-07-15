a = 32.50
b = 44.50

x = int(input("Digite a quantidade de horas trabalhadas: "))
A = x * a

y = int(input("Digite a quantidade de horas extras trabalhadas: "))
B = b * y

print(f"o salário bruto seu é: {A + B}")
z = A + B 
c = z / 0.11
print(f"O seu salário liquido é: {c}")