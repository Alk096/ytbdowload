class Livre:
    def __init__(self, titre:str, auteur:str, annee:int, disponible:bool = False):
        self.__titre = titre
        self.__auteur = auteur
        self.__annee = annee
        self.__disponible = disponible

    def emprunter(self):
        if self.__disponible == True:
            self.__disponible = False

    def retourner(self):
        if self.__disponible == False:
            self.__disponible = True

    def afficher_livre(self):
        print("======== Info du l ivre ==========")
        print(f"Titre : {self.__titre} | Auteur : {self.__auteur} | Annee : {self.__annee} | Disponibilite : {"Disponible" if self.__disponible else 'Pas Disponible'}")

    def __eq__(self, value):
        return ( 
            self.__titre == value.__titre
            and self.__auteur == value.__auteur
            and self.__annee == value.__annee
        )

    
class Membre:
    def __init__(self, nom:str , id_membre:int, emprunts:list = None):
        self.__nom = nom
        self.__id_membre = id_membre
        self.__emprunts = emprunts

    def emprunter_livre(self,livre):
        self.__emprunts.append(livre)

    
    def retourner_livre(self, livre):
        self.__emprunts.remove(livre)


    def afficher_membre(self):
        print("=========== Info Membre ============")
        print(f"Nom : {self.__nom}")
        print(f"Id Membre : {self.__id_membre}")
        