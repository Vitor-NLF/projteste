total = 0
pares = 0 
while True:
    n = int(input("Digite um número inteiro,(QUANDO QUISER SAIR DIGITE 0): "))
    if n == 0:
        break
    
    total = total + 1
    if n %2 == 0:
        pares = pares + 1
print("TOtal de números: ",total)
print("Total de valores pares é: ",pares)