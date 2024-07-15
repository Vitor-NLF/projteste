class Professor:
    def __init__(self,nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def hello (self):
        print(f"Olá {self.nome} sua idade é {self.idade} e seu sexo é {self.sexo}")

prof = Professor("Thiago",28,"Masculino")

prof.hello()