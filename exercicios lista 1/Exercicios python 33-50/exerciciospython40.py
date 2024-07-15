salario = float(input("Digite qual o salário base: "))
A = 0.05 * salario
B = salario + A
A2 = 0.07 * B
B2 =  B - A2
print(f"O resultado final do salário base é: {B2}")