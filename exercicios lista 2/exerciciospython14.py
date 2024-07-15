x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
if (x > y):
    print(f"O maior é: {x}")
elif (y > x):
    print(f"O maior é: {y}")
elif (x == x or y == y):
    print(f"NÚMEROS IGUAIS!!!")