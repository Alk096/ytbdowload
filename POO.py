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
    _id:int = 0
    def __init__(self, nom:str , emprunts:list = None):
        Membre._id+=1
        self._nom = nom
        self._id_membre = Membre._id
        self.__emprunts = emprunts if emprunts is not None else []

    def emprunter_livre(self,livre:Livre):
        livre.emprunter()
        self.__emprunts.append(livre)

    def retourner_livre(self, livre:Livre):
        livre.retourner()
        self.__emprunts.remove(livre)

    def afficher_membre(self):
        print("=========== Info Membre ============")
        print(f"Nom : {self._nom}")
        print(f"Id Membre : {self._id_membre}")

    def getNom(self):
        return self._nom
    
    def getId(self):
        return self._id_membre


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

    def supprimer_livre(self):
        print("============== Supprimer Livre =============")
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        annee = int(input("Annee : "))
        for livre in self.__livres:
            if livre == Livre(titre, auteur, annee):
                self.__livres.remove(livre)
                print("Le livre a ete supprimer")
                return
        print("Le livre n'est pas trouver")

    def ajouter_membre(self):
        print("========== Ajouter un membre =============")
        nom = input("Nom : ")
        self.__membres.append(Membre(nom))

    def supprimer_membre(self):
        print("============ Supprimer un membre ===========")
        nom = input("Nom : ")
        id = int(input("Id : "))
        for membre in self.__membres:
            if membre.getNom() == nom and membre.getId() == id:
                self.__membres.remove(membre)
                print("Membre supprimer")
                return
        print("Le memebre n'est pas trouver")

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
    
    def emprunter_livre(self):
        print("============ Emprunter Livre ======================")
        print("========== Membre Souhaitant Emprunter ============")
        membre = checherMembre(
            input("Nom : "),
            int(input("Id : ")),
            self.__membres
        )
        if not membre: return
        print("=================== Livre Desire ===================")
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        annee = int(input("Annee : "))
        livre = chercherLivre( titre, auteur, annee, self.__livres)
        if livre.est_disponible:
            membre.emprunter_livre(livre)


def checherMembre(nom:str, id:int,membres:list = None):
    membres = membres or []
    for membre in membres:
        if membre.getNom() == nom and membre.getId() == id:
            return membre
    print("Le membre n'est pas trouver")
    return None 
    
def chercherLivre( titre:str, auteur:str, annee:int, livres:list = None):
    livres = livres or []
    for livre in livres:
        if livre == Livre(titre,auteur,annee):
            return livre
    print("Le llivre n'est trouver")
    return None



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
        print("5. Supprimer un livre")
        print("6. Supprimer un Membre")
        print("7. Emprunter un livre")
        print("8. Retourner un livre")
        print("9. Affiche tout les livres")
        print("10. Quitter")
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
        elif choix == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            pkapkaLecture.supprimer_livre()
        elif choix == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            pkapkaLecture.supprimer_membre()
        elif choix == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            pkapkaLecture.emprunter_livre()
        elif choix == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choix == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choix == 10:
            os.system('cls' if os.name == 'nt' else 'clear')
            break


main()