

class Matiere:
    def __init__(self, name, coef):
        self.name= name
        self.coef= coef

    @property
    def name(self):
        return self.__name

    @property
    def coefficient(self):
        return self.__coefficient

    
    def __repr__(self):
        return 'matiere'