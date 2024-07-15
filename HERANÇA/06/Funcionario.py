class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

    def bater_ponto(self):
        lista = []
        while True:
            num = int(input("Deseja bater o ponto? 1 ou 0: "))
            if num == 1 or num == 0:
                lista.append(num)
            else:
                break

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)

        self.senha = senha

    def compras(self):
        print(f"O gerente {self.nome} está atendendo as demandas da empresa!!")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)

        self.comissao = comissao

    def bater_meta(self,vendas, meta):
        if vendas < meta:
            print(f"Você {self.nome} ainda precisa de {meta - vendas} vendas para bater a meta")
        else:
            print(f"Você {self.nome} ja bateu a meta")