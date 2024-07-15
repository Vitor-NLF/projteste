class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def AlterarPreco(self,novoValor):
        self.preco = novoValor
        print(f"Seu novo preço é: {novoValor}")
    
    def MostraSetor(self):
        print(f"Seu setor é {self.setor}")

##SUBCLASSES##
class IngressoVip(Ingresso):
    def __init__(self,preco,setor,camarote = bool,open_bar= bool,open_food= bool,estacionamento= bool):
        super().__init__(preco,setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def PegarBebida(self):
        if self.open_bar == True:
            print("Aqui está sua bebida!")
        else:
            print("Você não tem acesso as bebidas!")
    
    def AcessarCamarote(self):
        if self.camarote == True:
            print("Voce acessou o camarote")
        else:
            print("Voce nao pode acessar")

