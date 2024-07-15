x = float(input("Digite o valor: "))
A1 = 0.1 * x
B1 = x - A1
print(f"O total a pagar com o desconto de 10% fica: {B1}")

A2 = x / 3
print(f"O valor de cada parcela, parcelado em 3 vezes é: {A2}")

A3 = B1
z = 0.05 * A3
print(f"A comissão do vendedor, se for a vista, será de: {z}")

A4 = 0.05 * x
print(f"A comissão do vendedor, no caso da venda ser parcelada fica: {A4}")