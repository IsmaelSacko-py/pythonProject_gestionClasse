class Professeur:
    def __init__(self, nom , matiere, professeur):
        self.nom=nom
        self.matiere= matiere
        self.professeur= professeur

    def presentation(self):
        print(f"bonjour la classe je m'appelle mosieur{self.nom}")

    def Bye(self):
        print(f"aurevoir les etudiants")
        
    def speakMatiere(self):
        print(f"aujourd'hui on fais la matiere {self.matiere}")
