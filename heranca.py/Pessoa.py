class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

##SUBCLASSES##
class Aluno(Pessoa):
    def __init__(self,matricula,nome,idade,nota = None,media = None):
        super().__init__(matricula,nome,idade)
        self.nota = nota 
        self. media = media

    def caculo_media(self):
        lista1 = []
        self.nota = 0
        valor = 0
        self.media = valor
        while True:
            self.nota = float(input("Digite a sua nota: OU um número menor que 0 para parar!!:  "))
            if self.nota < 0:
                break
            lista1.append(self.nota)
        valor = sum(lista1) / len(lista1)
        print(valor)
    
    def estudadar(self):
        print(f"{self.nome} está estudando!")

class Professor(Pessoa):
    def __init__(self,matricula,nome,idade,formacao,disciplina,carga_horaria,salario):
        super().__init__(matricula,nome,idade)
        self.formacao = formacao 
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"{self.nome} está lecionando aula!")

