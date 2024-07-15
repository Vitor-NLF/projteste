n = int(input("Digite um número entre 100 e 9999: "))

while n < 100 or n > 9999:
    n = int(input("Número inválido! Digite um número entre 100 e 9999: "))

unidade = n % 10
n //= 10
dezena = n % 10
n //= 10
centena = n % 10
milhar = n // 10

print("Dezena: ",dezena)
print("Unidade: ",unidade)
print("Centena: ",centena)
print("milhar: ",milhar)
