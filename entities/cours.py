

class Cours:
    def __init__(self, Matiere, Professeur, Classe, date, Heure_debut, Heure_fin):
        self.__matiere = Matiere
        self.__professeur = Professeur
        self.__classe = Classe
        self.__date = Date
        self.__heure_debut = Heure_debut
        self.__heure_fin = Heure_fin

    def __repr__(self):
        return 'cours'