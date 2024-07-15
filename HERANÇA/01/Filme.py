class Filme:
    def __init__(self,nome=None,duracao=None):
        self.nome = nome 
        self.duracao = duracao

    def play(self):
        print(f"{self.nome} foi iniciado")


###SUBCLASSES###
class Acao(Filme):
    def __init__(self,nome,duracao,tiroteio):
        super().__init__(nome,duracao)
        self.tiroteio = tiroteio
    
    def emboscada(self):
        return(f"{self.tiroteio}, Na rua WestWill começou o tiroteio")
    

class Drama(Filme):
    def __init__(self,nome,duracao,momenttriste):
        super().__init__(nome,duracao)
        self.momenttriste = momenttriste
    
    def fazerChorar(self):
        return (f"{self.momenttriste}. Isso Começou a te fazer chorar!!")


class Suspense(Filme):
    def __init__(self,nome,duracao,medo):
        super().__init__(nome,duracao)
        self.medo = medo 
    
    def susto(self):
        return (f"{self.medo} Boooooo")
    

