class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self,valor):
        if valor > 0:
            novoSaldo = valor + self.saldo
            print("Após o depósito, seu saldo atual passa a ser: ",novoSaldo)
        else:
            print("SALDO NEGATIVO!!")
    def saque(self,valor):
        novoSaldo =  self.saldo - valor
        print("Após o saque, seu saldo atual passa a ser: ",novoSaldo)

    def imprimirSaldo(self):
        print("SALDO: ",self.saldo)



p1 = Conta("ADRIANE",5555,2222,10500)
print(p1.imprimirSaldo())
x = int(input("O que você deseja: (1 - SACAR OU 2 - DEPOSITAR)"))
if x == 1:
    valor = float(input("DIGITE O VALOR PARA SAQUE: "))
    p1.saque(valor)
elif x == 2:
    valor = float(input("DIGITE O VALOR PARA DEPOSITO: "))
    p1.depositar(valor)
else:
    print("OPÇÃO INVÁLIDA!!!")