from personne import Personne

class eleve(Personne):

    def __init__(Name : str, Surname : str, Age : int):
        super().__init__(Name, Surname, Age)