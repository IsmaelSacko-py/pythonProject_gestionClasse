

class Cours:
    def __init__(self, Matiere, Professeur, Classe, date, Heure_debut, Heure_fin):
        self.__matiere = Matiere
        self.__professeur = Professeur
        self.__classe = Classe
        self.__date = Date
        self.__heure_debut = Heure_debut
        self.__heure_fin = 
        

    @property
    def matiere(self):
        return self.__matiere

    @property
    def professeur(self):
        return self.__professeur
    
    @property
    def classe(self):
        return self.__classe

    @property
    def date(self):
        return self.__date

    @property
    def heure_debut(self):
        return self.__heure_debut

    @property
    def heure_fin(self):
        return self.__heure_fin

    

    def __repr__(self):
        return 'cours'