

class Classe:
    def __init__(self, Niveau : str):
        self.__niveau = Niveau

    def __repr__(self):
        return 'classe'
    
seconde= Classe("seconde")
premiere= Classe("premiere")
terminale= Classe("terminale")

nosClasses= [seconde, premiere, terminale]