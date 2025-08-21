import os
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
        print("======== Info du livre ===========")
        print(f"Titre : {self.__titre} | Auteur : {self.__auteur} | Annee : {self.__annee} | Disponibilite : {"Disponible" if self.__disponible else 'Pas Disponible'}")

    def est_disponible(self):
        return self.__disponible

    def __eq__(self, value):
        return ( 
            self.__titre == value.__titre
            and self.__auteur == value.__auteur
            and self.__annee == value.__annee
        )

    
class Membre:
    _id = 0
    def __init__(self, nom:str , emprunts:list = None):
        Membre._id+=1
        self._nom = nom
        self._id_membre = Membre._id
        self.__emprunts = emprunts if emprunts is not None else []

    def emprunter_livre(self,livre):
        self.__emprunts.append(livre)

    
    def retourner_livre(self, livre):
        self.__emprunts.remove(livre)


    def afficher_membre(self):
        print("=========== Info Membre ============")
        print(f"Nom : {self._nom}")
        print(f"Id Membre : {self._id_membre}")


class Bibliotheque:
    def __init__(self, livres:list = None, membres:list = None):
        self.__livres = livres if livres is not None else []
        self.__membres = membres if membres is not None else []

    def ajouter_livre(self):
        print("============== Ajouter un livre =========")
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        annee = int(input("Annee : "))
        self.__livres.append(Livre(titre, auteur, annee))

    # supprimer livre

    def ajouter_membre(self):
        print("========== Ajouter un membre =============")
        nom = input("Nom : ")
        self.__membres.append(Membre(nom))

    # supprimer membre

    def afficher_livre_disponible(self):
        print("======== Livre disponible ==========")
        di = False
        for livre in self.__livres:
            if livre.est_disponible():
                di = True
                livre.afficher_livre()
        if not di:
            print("Vous n'avez accun livre de disponible")

    def afficher_membre(self):
        print("============ Membre de la bibliotheque ==========")
        for membre in self.__membres:
            membre.afficher_membre()


livres_test = [
    Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, True),
    Livre("1984", "George Orwell", 1949, True),
    Livre("L'Étranger", "Albert Camus", 1942, False)
]

# Liste de membres prédéfinis
membres_test = [
    Membre("Alice"),
    Membre("Bob"),
    Membre("Charlie")
]


def main():
    pkapkaLecture = Bibliotheque(livres_test, membres_test)
    while True:
        print("========= Menu bibliotheque ===========")
        print("1. Ajouter un llivre")
        print("2. Ajouter un Membre")
        print("3. Afficher livre disponible")
        print("4. Afficher Membres")
        # print("7. Rehercher livre")
        print("8. Quitter")
        choix = int(input("Choix : "))
        if choix == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            pkapkaLecture.ajouter_livre()
        elif choix == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            pkapkaLecture.ajouter_membre()
        elif choix == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            pkapkaLecture.afficher_livre_disponible()
        elif choix == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            pkapkaLecture.afficher_membre()
        elif choix == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            break


main()