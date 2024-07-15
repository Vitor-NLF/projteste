class Pessoa:
     def __init__(self,nome,idade,endereco):
          self.nome = nome
          self.idade = idade
          self.endereco = endereco
     
     def getNome(self):
          return self.nome
     
     def setIdade(self,novaIdade):
          self.idade = novaIdade

pessoa1 = Pessoa(1, "Wendril",18)

print(pessoa1.id)
print(pessoa1.getNome())
print(pessoa1.idade)
print("######"*9)
