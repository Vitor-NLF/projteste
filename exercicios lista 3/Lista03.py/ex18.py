quantidade = int(input("digite a quantidade de numeros: "))

n = int(input("Digite um número: "))


while quantidade > 1:
    n2 = int(input("Digite um número: "))
    if n2 > n:
        n = n2
    quantidade -= 1

print("o maior é: ", n )