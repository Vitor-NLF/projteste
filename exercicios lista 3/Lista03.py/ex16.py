n = int(input("Digite um número: "))
i = 1
if n %2 != 0:    
    while i <= n:
        print(i)
        i = i + 2
else:
    print("O número digitado não é ímpar!!")