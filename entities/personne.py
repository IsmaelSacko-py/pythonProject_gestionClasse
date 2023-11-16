from datetime import datetime
class Personne:
    def __init__(self, Name : str, Surname : str, Age : int):
        self._name = Name
        self._surmane = Surname
        self._age = Age
        self._matricule = self._name[0].upper() + self._surname[0].upper() + str(self._age)

    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def age(self):
        return self._age
    
    @property
    def matricule(self):
        return self._matricule