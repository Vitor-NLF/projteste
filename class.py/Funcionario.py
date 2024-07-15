class Funcionario:
    def __init__(self,nome,sobrenome,horastrabalhadas,valorhora):
        self.nome = str(nome)
        self.sobrenome = str(sobrenome)
        self.horastrabalhadas = horastrabalhadas
        self.valorhora = valorhora

    def nomeCompleto(self):
        nomeCompleto = self.nome + self.sobrenome
        print(nomeCompleto)

    def calculSalario(self):
        novoSalario = self.horastrabalhadas * self.valorhora
        print("Seu salário é de: ",novoSalario)

    def alterarDados(self,valorhora):
        novaHora = valorhora
        print("O novo valor por horas trabalhadas é: ", novaHora)

p1 = Funcionario("Vitor ","Nascimento",45,46)
p1.nomeCompleto()
p1.calculSalario()
x = float(input("Digite o no valor por hora: "))
p1.alterarDados(x)
