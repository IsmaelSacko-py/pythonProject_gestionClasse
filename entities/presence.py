

class Presence:
    def __init__(self, Eleve, Cours, Date, Present):
        
        self.__eleve = Eleve
        self.__cours = Cours
        self.__date = Date
        self.__present = Present

    
    @property
    def eleve(self):
        return self.__eleve

    @property
    def cours(self):
        return self.__cours

    @property
    def date(self):
        return self.__date

    @property
    def present(self):
        return self.__present

    

    def __repr__(self):
        return 'presence'