class Circulo:
    def __init__(self,raio):
        self.raio = raio
    
    def imprimirValor(self,raio):
        print("O raio é: ",raio)
    
    def calcularArea(self):
        area = 3.14 * (self.raio**2)
        print("A area do circulo é; ",area)
    def calcularCircunferencia(self):
        circunferencia = (3.14**2)*self.raio
        print("A circunferência do círculo é: ",circunferencia)

raio = float(input("Digite o valor do raio: "))
circulo1 = Circulo(raio)
circulo1.imprimirValor(raio)
circulo1.calcularArea()
circulo1.calcularCircunferencia()