class Agenda:
    def __init__(self,dia,mes,ano,anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validarData(self):
        if self.dia > 31 or self.mes > 13 or self.ano < 2024:
            print("Data inválida")
        else:
            print("DATA CORRETA")
    
    def anotarTarefa(self,tarefa):
        self.notacao = tarefa
        print("AGORA SUA NOVA ANOTAÇÃO É",tarefa)
        
    
    def mostrarAnotacao(self):
        print("Sua anotação é: ",self.anotacao)
    
dia = int(input("Digite o dia: "))
mes = int(input("DIgite o mes: "))
ano = int(input("Digite o ano: "))
anotacao = input("Digite uma anotacao: ")
agend = Agenda(dia,mes,ano,anotacao)
agend.validarData()
agend.mostrarAnotacao()
tarefa = input("Digite uma nova anotação: ")
agend.anotarTarefa(tarefa)