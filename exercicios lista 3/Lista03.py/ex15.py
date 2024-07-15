n = int(input("Digite um número par: "))

if n %2 == 0:
    while n >= 0:
        print (n)
        n = n - 2
       
else:
    print("Número digitado não é par")