print("Olá, bom dia!")
a = int(input("Digite a sua idade por favor: "))
b = float(input("Digite o tempo de serviço que você contribuiu: "))
if(a >= 65):
    print("A sua idade ja permite que se aposente!!")
elif(b >= 30):
    print("O seu tempo de trabalho é maior que 30 anos, então já pode se aposentar!")
elif(a >= 60) and (b >= 25):
    print("Você tem mais de 60 anos! E já trabalhou 25 anos! Então já pode se aposentar!!")