sexo = input("Olá, poderia me falar seu sexo? ")
altura = float(input("E sua altura: "))

if (sexo == "Masculino") or (sexo == "MASCULINO") or (sexo =="masculino"):
    x = (72.7 * altura) - 58
    print(f"Seu peso idela é: {x}")

elif (sexo =="Feminino") or (sexo == "FEMININO") or (sexo == "feminino"):
    z = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {z}")