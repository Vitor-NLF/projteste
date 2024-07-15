class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel=5):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano 
        self.valor = valor
        self.nivel = nivel

    def calcularImposto(self):
        imposto = (self.valor * 3) / 100
        return imposto

    def abastecer(self,quant_litros):
        self.nivel = self.nivel + quant_litros

    def andar(self,km):
       consumo = km / 10.8
       self.nivel = self.nivel - consumo

    def verificarNivel(self):
        return self.nivel

car1 = Carro("Jetta","Volks","Branco",2022,180000) 
print(car1.calcularImposto())

print("NÍVEL DE GASOLINA: ",car1.nivel," litros")
car1.abastecer(50)
print("NÍVEL DE GASOLINA: ",car1.nivel," litros")
car1.andar(250)
tanque = car1.verificarNivel()
print(f"{tanque: 2f}")