print("Olá, escolha uma das opções abaxo...")
print("1. Soma e dois números")
print("2. Diferença entre dois números (MAIOR PELO MENOR)")
print("3. Produto entre dois números")
print("4. Divisão entre dois números")

A = int(input("Digite o número da opção desejada: "))

if(A == "1"):
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))
    c = a + b 
    print("O resultado é: {c}")
elif(A == "2"):
    a1 = float(input("Digite um número: "))
    b1 = float(input("Digite outro número: "))
    c1 = a1 - b1
    print(f"A diferença é: {c1}")
elif(A == "3"):
    a2 = float(input("Digite um número: "))
    b2 = float(input("Digite outro número: "))
    c2 = a2 * b2
    print(f"O produto dos números é: {c2}")
elif(A == "4"):
    a3 = float(input("Digite um número: "))
    b3 = float(input("Digite outro número: "))
    c3 = a3 / b3
    print(f"O resultado da divisão é: {c3}")