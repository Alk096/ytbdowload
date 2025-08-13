#ajout
"""
    append() : Ajouter un item à la fin de la liste
    insert() : Ajouter un item à une position spécifique
    extend() : Ajouter plusieurs items à la fin de la liste
"""
#supprimer
"""
    remove(item) : Supprimer un item spécifique de la liste
    pop() : Supprimer le dernier item de la liste
    pop(index) : Supprimer un item à une position spécifique
    clear() : Supprimer tous les items de la liste
    del list[index] : Supprimer un item à une position spécifique
    del list[start:end] : Supprimer une tranche d'items de la liste
    del list : Supprimer la liste entière
"""
#operations
"""
    len(l) : Obtenir la longueur de la liste
    count(item) : Compter le nombre d'occurrences d'un item dans la liste
    l.sort() : Trier la liste en place
    l.sort(reverse=True) : Trier la liste en place dans l'ordre inverse
    l.sort(key=len) : Trier la liste en place selon la longueur des items
    sorted(l) : Retourner une nouvelle liste triée
    l.reverse() : Inverser l'ordre des items dans la liste
    min(l) : Obtenir le plus petit item de la liste
    max(l) : Obtenir le plus grand item de la liste
"""
#recherche
"""
    index(item) : Obtenir l'index du premier item correspondant
    index(item, start, end) : Obtenir l'index du premier item correspondant dans une plage
    in : Vérifier si un item est présent dans la liste
    not in : Vérifier si un item n'est pas présent dans la liste
"""
#duplication
"""
    l.copy() : Créer une copie superficielle de la liste

"""
#parcourir une liste
"""
    for item in l : Parcourir les items de la liste
    for index, item in enumerate(l) : Parcourir les items avec leurs index
    for item in range(len(l)) : Parcourir les index de la liste
    for item, next_item in zip(l, l[1:]) : Parcourir les items et leurs suivants
    for a, b, c in zip(l1, l2, l3) : Parcourir plusieurs listes en parallèle
    for item in l if condition : Parcourir les items qui satisfont une condition
"""


def ajouterNom(list = []):
    item = input('Nom : ')
    list.append(item)


def afficherNom(list = []):
    print('======= Affichage de la List =========')
    for item in list:
        print(item)
    #for item in range(len(list)):
        #    print(list[item])
    #for index, item in enumerate(list):
    #    print(f'Index : {index}, Item : {item}')
    #for langues, noms, agees in zip(langues, noms, agees):
    #    print(f'Langue : {langues}, Nom : {noms}, Age : {agees}')


def supprimerNom(list = []):
    print('========= Suppression d\'un item de la liste ========')
    item = input('Nom : ')
    return list.remove(item)


def supprimerDernierItem(list = []):
    list.pop()
    print('========== Dernier Item supprimer ==========')



def possition(list = []):
    print('========= La possion d\'un item de la liste ===========')
    try:
        item = input('Nom : ')
        print(list.index(item) + 1)
    except ValueError as e :
        print(f'Error : {e}')

# creation d'une liste imbriquée
ListeImbrique = [
    'Programming Languages',
    ['Python', 'Java', 'C++'],
    [25, 30, 35],
    'Bob',
]
#creation d'une matrice
Matrice = []

def creerMatrice(lignes, colonnes):
    global Matrice
    for i in range(lignes):
        lignes = []
        for j in range(colonnes):
            lignes.append(input(f'Entrez l\'élément de la position ({i+1},{j+1})'))
        Matrice.append(lignes)

def afficherMatrice(list = []):
    print('========= Affichage de la Matrice =========')
    for ligne in range(len(list)):
        for colonnes in range(len(list[ligne])):
            print(f'{list[ligne][colonnes]}, ({ligne+1},{colonnes+1})')

def main():
    global Matrice
    print('========= Bienvenue dans la liste ==========')
    creerMatrice(3,3)
    afficherMatrice(Matrice)



main()