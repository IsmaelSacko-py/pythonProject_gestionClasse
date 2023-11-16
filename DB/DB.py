import sqlite3 as sql3
# from abc import ABC, abstractmethod


DB_NAME = "DB/DB.sqlite"

class DB:
        
        
    def getConnexion(self):

        try:
            self.__connexion = sql3.connect(DB_NAME)
            self.__cursor = self.__connexion.cursor()

            print("connexion etablie")
            return self.__connexion, self.__cursor

        except Exception as e:
            print(f"Erreur lors de la connexion a la base de donnees [{e}]")
            exit(-1)

        # finally:
        #     return self.__connexion, self.__cursor
        
    def add(self, entitie):

        match entitie:
            case 'eleve':
                request = "INSERT INTO eleve(nom, prenom, date_naissance, id_classe) VALUES(?, ?, ?, ?)"
                self.__cursor.execute(request, (entitie.name, entitie.surname, entitie.age, entitie.matricule))
                self.__connexion.commit()

            case 'professeur':
                request = "INSERT INTO professeur(nom, prenom, id_matiere) VALUES(?, ?, ?)"
                self.__cursor.execute(request, (entitie.name, entitie.surname, entitie.matiere))
                self.__connexion.commit()

            case 'matiere':
                request = "INSERT INTO matiere(nom, coefficient) VALUES(?, ?)"
                self.__cursor.execute(request, (entitie.name, entitie.coefficient))
                self.__connexion.commit()

            case 'classe':
                request = "INSERT INTO classe(niveau) VALUES(?)"
                self.__cursor.execute(request, (entitie.niveau))
                self.__connexion.commit()

            case 'cours':
                request = "INSERT INTO cours(id_matiere, id_professeur, id_classe, date, heure_debut, heure_fin) VALUES(?, ?, ?, ?, ?, ?)"
                self.__cursor.execute(request, (entitie.matiere, entitie.professeur, entitie.classe, entitie.date, entitie.heure_debut, entitie.heure_fin))
                self.__connexion.commit()

            case 'presence':
                request = "INSERT INTO presence(id_eleve, id_cours, date, present) VALUES(?, ?, ?, ?)"
                self.__cursor.execute(request, (entitie.eleve, entitie.cours, entitie.date, entitie.present))
                self.__connexion.commit()

            case _:
                print(f'la classe {entitie} est inexistante')

    def delete(self, id : int, entitie : str):
        entitie = entitie.__repr__()
        request = f"DELETE FROM {entitie.lower()} WHERE id{entitie.capitalize()} = ?"
        self.__cursor.execute(request, (id, ))
        self.__connexion.commit()

    def getAll(self, entitie : str) -> list:
        entitie = entitie.__repr__()
        request = f"SELECT * FROM {entitie.lower()}"
        self.__cursor.execute(request)
        return self.__cursor.fetchall()

    def getOne(self, id, entitie:str) -> list:
        entitie = entitie.__repr__()
        request = f"SELECT * FROM {entitie.lower()} WHERE id{entitie.lower()} = ?"
        self.__cursor.execute(request, (id, ))
        return self.__cursor.fethone()