class Passagem:
    def __init__(self,preco,assento):
        self.preco = preco
        self.assento = assento

    def AlternaPreco(self,novoPreco):
        self.preco = novoPreco
        print(novoPreco)

    def escolherAssento(self):
        self.assento = int(input("Digite o número do assento: "))
        print(self.assento)


class PassagemBus(Passagem):
    def __init__(self,preco,assento,placa,leitor):
        super().__init__(preco,assento)
        self.placa = placa
        self.leitor = leitor 
    
    def abastecer(self):
        print(f"O ônibus placa {self.placa} está abastecendo!!")

class PassagemAviao(Passagem):
    def __init__(self,preco,assento,portaodeembarque,checkin):
        super().__init__(preco,assento)
        self.portaodeembarque = portaodeembarque
        self.checkin = checkin

    def decolar(self):
        print(f"O avião está decolando pelo portão de embarque {self.portaodeembarque}")