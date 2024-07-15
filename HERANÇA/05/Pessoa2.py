class Pessoa2:
    def __init__(self,nome,telefone,email,endereco):
        self.nome = nome 
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está negociando!")
    
class PessoaFisica(Pessoa2):
    def __init__(self, nome,telefone,email,endereco,cpf):
        super().__init__(nome,telefone,email,endereco)
        self.cpf = cpf
    
    def comprar(self):
        print(f"{self.nome} está comprando como pessoa física!")


class PessoaJuridica(Pessoa2):
    def __init__(self, nome,telefone,email,endereco,cnpj):
        super().__init__(nome,telefone,email,endereco)
        self.cnpj = cnpj
    
    def vender(self):
        print(f"{self.nome} está vendendo como pessoa jurídica!")