a = int(input("Digite o ano para que possamos saber se ele é bissexto ou não: "))

if(a / 400) and (a / 4) and not (a / 100):
    print("O ano digitado é bissexto!!")
else:
    print("O  ano não é bissexto!!")

