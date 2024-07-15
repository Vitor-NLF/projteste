print("Olá bem vindo a cálculadora!!!")
x = input("Vc gostaria de multiplicar, dividir, subtrair ou somar? ")
if(x == "multiplicar") or (x == "Multiplicar") or (x == "MULTIPLICAR"):
    print("ENTÃO VAMOS MULTIPLICAR!!")
    a1 = float(input("digite o primeiro número para possamos multiplicar: "))
    b1 = float(input("digite outro número: "))
    r1 = a1 * b1 
    print(f"O resultado da multiplicação é: {r1}")

elif(x == "dividir") or (x == "Dividir") or (x == "DIVIDIR"):
    print("ENTÃO VAMOS DIVIDIR!!")
    a2 = float(input("digite o primeiro número para que possamos dividir: "))
    b2 = float(input("digite outro número: "))
    r2 = a2 / b2 
    print(f"O resultado da divisão é: {r2}")

elif(x == "subtrair") or (x == "Subtrair") or (x == "SUBTRAIR"):
    print("ENTÃO VAMOS SUBTRAIR!!")
    a3 = float(input("digite o primeiro número para que possamos subtrair: "))
    b3 = float(input("Digite outro número: "))
    r3 = a3 - b3
    print(f"O resultado final da subtração: {r3}")

elif(x == "somar") or (x == "Somar") or (x == "SOMAR"):
    print("ENTÃO VAMOS SOMAR!!")
    a4 = float(input("digite o primeiro número para que possamos somar: "))
    b4 = float(input("digite outro número: "))
    r4 = a4 + b4
    print(f"o resultado final da soma é: {r4}")
