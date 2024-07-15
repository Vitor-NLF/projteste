print("Olá, digite suas notas abaixo!!(de 0 a dez)")
a = float(input("\ndigite a primeira nota (trabalho): "))
b = float(input("\ndigite a segunda nota (avaliação semestral):"))
c = float(input("\ndigite a terceira nota (exame final): "))

A = a * 2
B =  b * 3
C = c * 5
D =  5 + 3 + 2
R = (A + B + C) / D
print("\n A NOTA É: ",R)

if(R >= 0) and (R <= 2.9):
    print("O ALUNO ESTÁ REPROVADO!!")
elif(R >= 3) and (R <= 5.9):
    print("O ALUNO ESTÁ DE RECUPERAÇÃO!!!")
elif(R >= 6.0):
    print("O ALUNO ESTÁ APROVADO!!!!")