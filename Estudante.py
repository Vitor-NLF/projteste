class Estudante:
    def __init__(self,matricula,nome,idade,nota):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def hello(self):
        print(f"Olá {self.nome}")

    def mostrarDados(self):
        print(f" Matricula: {self.matricula}")
        print(f" Nome: {self.nome}")
        print(f" Idade: {self.idade}")
        print(f" Nota: {self.nota}")


aluno2 = Estudante(1313,"Domitila",18,80)

aluno2.nome = "Ana Patrícia"

aluno2.mostrarDados()