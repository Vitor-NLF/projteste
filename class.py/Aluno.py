class Aluno:
    def __init__(self,nome, ra, nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def getSituação(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        print(media)
        if media >= 7:
            print("APROVADO")
        elif media < 5:
            print("REPROVADO")
        else:
            print("EXAME")
nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

nota = Aluno("Pablo",5455.444,nota1,nota2,nota3,nota4)
nota.getSituação()