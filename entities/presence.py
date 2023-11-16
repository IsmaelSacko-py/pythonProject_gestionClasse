

class Presence:
    def __init__(self, Eleve, Cours, Date, Present):
        
        self.__eleve = Eleve
        self.__cours = Cours
        self.__date = Date
        self.__present = Present

    def __repr__(self):
        return 'presence'