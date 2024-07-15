class Livro:
    def __init__(self,nome, autor, editora, paginas ):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    

    def setEditora(self):
        novaEditora = input("Digite o nome da nova editora: ")
        self.editora = novaEditora
        print(f"Editora: {self.editora}")
        livroo.getDados()

    def mostrarPaginas(self):
        print(f"{self.paginas} Páginas")

    def getDados(self):
        print("Nome do livro: ", self.nome)
        print("Nome do autor: ",self.autor)
        print("Nome da editora: ",self.editora)
        print("Quantidade de páginas: ",self.paginas)
        return self.getDados
         
livroo = Livro("Harry Potter","Luiz","Magia",150)
print(livroo)
livroo.getDados()
livroo.setEditora()
livroo.mostrarPaginas()