x = float(input("Digite quantas horas foram trabalhadas: "))
a = x * 40.50
if(a < 2500):
    print("O salario liquido final é de: ", a)

elif(a > 2500):
    b = 0.11 * a
    print("O salario liquido final é de: ", b)