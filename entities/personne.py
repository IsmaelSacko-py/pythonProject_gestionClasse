from datetime import datetime
class Personne:
    def __init__(self, Name : str, Surname : str, Age : int):
        self._name = Name
        self._surmane = Surname
        self._age = Age
        self._matricule = self._name[0].upper() + self._surname[0].upper() + str(self._age)
