x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))
if((x >= 0 and y >= 0) and (x <= 10.0 and y <= 10.0)):
    A = (x + y) / 2
    print(f"\nA média das notas é: {A}")
    print("O valor é válido")
else:
    print("O VALOR DADO NÃO É VÁLIDO!!")