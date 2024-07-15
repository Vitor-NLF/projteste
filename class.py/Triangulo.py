class Triangulo:
    def __init__(self,ladoa,ladob,ladoc):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc

    def suaArea(self):
        ladoh = self.ladoa + self.ladob
        calculo = 1/2 * self.ladoc * ladoh
        print(calculo)
    
    def maiorLado(self):
        print ("O maior lado é :",max(self.ladoa,self.ladob,self.ladoc))

h = float(input("Digite um lado do triângulo: "))
h2 = float(input("Digite o outro lado do triângulo: "))
b = float(input("Digite a base do triângulo: "))

triag = Triangulo(h,h2,b)
triag.suaArea()
triag.maiorLado()