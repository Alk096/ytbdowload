import os
classe = [
    ["Amina", [15, 17, 14]],
    ["Karim", [12, 9, 13]],
    ["Sali", [18, 20, 19]],
    ["Moussa", [8, 11, 10]],
]


def ajouterEtudiant(cl = []):
    etudiant = []
    note = []
    nom = input("Entrez le nom de l'étudiant :")
    etudiant.append(nom)
    for i in range(3):
        note.append(float(input(f"Emtrez la note {i+1} de {nom} :")))
    cl.append([etudiant, note])

def afficherClasse(cl = []):
    if not cl:
        print("La classe est vide.")
    else:
        print("Liste des étudiants et leurs notes :")
        for etudiant in cl:
            print(etudiant)

def afficherEtudiants( cl = [] ):
    if not cl:
        print("La classe esrt vide.")
    else:
        print("Liste des étudiants :")
        for etudiant in cl:
            print(etudiant[0])

def afficherEtudiantsEtNotes(cl = []):
    if not cl:
        print("La classe est vide.")
    else:
        print("Liste des étudiants et leurs notes : ")
        for etudiant in cl:
            print(f"Etudiant : {etudiant[0]}, Notes : {etudiant[1]}")
    
def afficherEtudiantsMoyennes(cl = []):
    if not cl:
        print("La classe est vide.")
    else:
        print("Liste des étudiants et leurs moyennes :")
        for etudiant in cl:
            print(f"Etudiant : {etudiant[0]},Moyenne : {sum(etudiant[1])/len(etudiant[1])}")

def mettreAJourNomEtudiant(cl = [], nomActuel = "", nouveauNom = ""):
    for etudiant in cl:
        if etudiant[0] == nomActuel:
            etudiant[0] = nouveauNom
            print(f"Le nom de l'étudiant a été mis à jour de {nomActuel} à {nouveauNom}.")
            return
    print(f"Aucun étudiant trouvé avec le nom {nomActuel}.")

def mettreAJourNotesEtudiant(cl = [], nom = ""):
    for etudiant in cl:
        if etudiant[0] == nom and etudiant[1]:
            notes = []
            for i in range(len(etudiant[1])):
                notes.append(float(input(f"Entrez la nouvelle note {i+1} pour {nom} : ")))
            etudiant[1] = notes
            print(f"Les notes de l'étudiant {nom} ont été mises à jour.")


def mettreAJourNoteEtudiant(cl = [], nom = ""):
    noteIndex = int(input(f"Entrez la position de la note à modifier pour {nom} (1,2 ou 3) :"))
    note = float(input(f"Entrez la nouvelle note : "))
    if noteIndex < 1 or noteIndex > 3:
        print("Les etudiant on que 3 notes.")
        return
    for etudiant in cl:
        if etudiant[0] == nom:
            etudiant[1][noteIndex - 1] = note
            print(f"La note {noteIndex} de l'étudiant {nom} a été mise à jour.")
            return


def supprimerEtudiant(cl = [], nom = ""):
    for etudiant in cl:
        if etudiant[0] == nom:
            cl.remove(etudiant)
            print(f"L'étudiant {nom} a été supprimé de la classe.")
            return



def main():
    while True:
        print("\nMenu")
        print("1. Ajouter un étudiant")
        print("2. Afficher la classe")
        print("3. Afficher la liste des étudiants")
        print("4. Afficher la liste des etudiants et leurs notes")
        print("5. Afficher la liste des etudiants et leurs moyennes")
        print("6. Mettre à jour le nom d'un étudiant")
        print("7. Mettre à jour les notes d'un étudiant")
        print("8. Mettre à jour une note d'un étudiant")
        print("9. Supprimer un étudiant")
        print("10 . Quitter")
        choix = int(input("Entrez votre choix : "))
        if choix == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ajout d'un étudiant :")
            ajouterEtudiant(classe)
        elif choix == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Affichage de la classe :")
            afficherClasse(classe)
        elif choix == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            afficherEtudiants(classe)
        elif choix == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            afficherEtudiantsEtNotes(classe)
        elif choix == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            afficherEtudiantsMoyennes(classe)
        elif choix == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            mettreAJourNomEtudiant(classe,
                input("Entrez le nom à modifer : "),
                input("Entrez le noveau nom :")
            )
        elif choix == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            mettreAJourNotesEtudiant(classe,
                input("Entrez le nom de l'étudiant dont vous voulez mofier les notes : ")
            )
        elif choix == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            mettreAJourNoteEtudiant(classe,
                input("Entrez le nom de l'étudiant dont vous voulez modifier une note : ")
            )
        elif choix == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            supprimerEtudiant(classe,
                input("entrez le nom de l'étudiant à supprimer : ")                  
            )
        elif choix == 10:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Au revoir!")
            break


main()