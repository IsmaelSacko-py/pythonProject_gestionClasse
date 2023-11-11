from personne import Personne

class Professeur(Personne):
    def __init__(self, Name : str , Surname : str, Age: int):
        self._name = Name
        self._surmane = Surname
        self._age = Age
        self._matricule = self._name[0].upper() + self._surname[0].upper() + str(self._age)

    def presentation(self):
        print(f"bonjour la classe je m'appelle mosieur{self.nom}")

    def Bye(self):
        print(f"aurevoir les etudiants")
        
    def speakMatiere(self):
        print(f"aujourd'hui on fais la matiere {self.matiere}")
