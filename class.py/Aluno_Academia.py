class Aluno_Academia:
    def __init__(self,nome,idade,peso,altura,mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade 

    def calcularIMC(self,peso,altura):
        calculo = peso / (altura**2)
        print("Seu IMC é: ",calculo)
    
    def obterValorMens(self):
        print("Valor da mensalidade: ",self.mensalidade)
        if idade <= 17:
            print("Você é de menor, GANHOU UM DESCONTO!")
            print("Valor final da mensalidade R$80")

        elif idade >= 18:
            print("Você não é de menor, NÃO GANHOU DESCONTO!!")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pessoa = Aluno_Academia(nome,idade,peso,altura)
pessoa.calcularIMC(peso,altura)
pessoa.obterValorMens()
