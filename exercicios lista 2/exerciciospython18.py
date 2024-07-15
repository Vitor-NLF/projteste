salario = float(input("Digite seu salario: "))
prestacao = float(input("Digite o valor da prestação de um empréstimo: "))

a = 0.2 * salario

if(prestacao > a ):
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")    