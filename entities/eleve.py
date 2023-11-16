from entities.personne import Personne
from entities.classe import *


class Eleve(Personne):

    def __init__(self, Name : str, Surname : str, Age : int, classe: Classe):
        super().__init__(Name, Surname, Age)
        self.__myclass= classe

    def inscription(self):
        Nom= input("veuillez saisir votre nom: ")
        prenom= input("veuillez saisir votre prenom: ")
        for i in nosClasses:
            print (f"{i.number}")
        while VotreClasse <1 or  VotreClasse > 3:
            VotreClasse= input("en quelle voulez vous vous inscrire(veuillez saisir le chiffre): ")
        StudentClasse= nosClasses[VotreClasse-1]

        return Nom , prenom , StudentClasse

    def __repr__(self):
        return 'eleve'
