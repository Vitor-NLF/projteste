def carro(kilometros, consumidos):
    kmlitro = kilometros / consumidos

    if kmlitro < 8:
        print("Venda o carro!")
    elif kmlitro >= 8 and kmlitro <= 15:
        print("Êconomico!")
    elif kmlitro > 15:
        print("Super economico")
    else:
        print("erro")

kilometro = float(input("Digite o km: "))
consumido = float(input("Digite o consumo: "))

carro(kilometro,consumido)