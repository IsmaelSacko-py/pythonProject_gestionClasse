from entities.personne import Personne

class Professeur(Personne):
    def __init__(self, Name : str , Surname : str, Matiere):
        self._name = Name
        self._surmane = Surname
        self._matiere = Matiere

    def presentation(self):
        print(f"bonjour la classe je m'appelle mosieur{self.nom}")

    def Bye(self):
        print(f"aurevoir les etudiants")
        
    def speakMatiere(self):
        print(f"aujourd'hui on fais la matiere {self.matiere}")

    def __repr__(self):
        return 'professeur'
