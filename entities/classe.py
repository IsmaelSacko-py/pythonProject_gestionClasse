

class Classe:
    num_classe = 0
    def __init__(self, Name : str):
        Classe.num_classe += 1
        self.name = Name
        self.number = self.name + '_' + str(Classe.num_classe)
    
seconde= Classe("seconde")
premiere= Classe("premiere")
terminale= Classe("terminale")

nosClasses= [seconde, premiere, terminale]