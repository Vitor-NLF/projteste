i = 0
soma = 0 
cont = 0
while i == 0:
    x = float(input("Digite as notas, DIGITE 0 QUANDO QUISER PARAR!: "))
    soma = soma + x
    cont = cont + 1 
    if x > 10:
        print("NÚMERO INVÁLIDO!")
    if x < 0:
        print("NÚMERO INVÁLIDO")
    elif x == 0:
        break
cont = cont - 1
media = soma/cont    
print("A soma das notas é: ",soma)
print("A média das notas é: ",media)