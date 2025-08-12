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
    l.reverse() : Inverser l'ordre des items dans la liste
    min(l) : Obtenir le plus petit item de la liste
    max(l) : Obtenir le plus grand item de la liste
"""
#recherche
"""
    index(item) : Obtenir l'index du premier item correspondant
    in : Vérifier si un item est présent dans la liste
    not in : Vérifier si un item n'est pas présent dans la liste
"""
#duplication
"""
    copy() : Créer une copie superficielle de la liste

"""


def ajouterNom(list = []):
    item = input('Nom : ')
    list.append(item)


def afficherNom(list = []):
    print('======= Affichage de la List =========')
    for item in list:
        print(item)


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
        print(list.indexof(item) + 1)
    except ValueError as e :
        print(f'Error : {e}')


def main():
    listNom = ['Alker','Pap','Moussa']
    # ajouterNom(listNom)
    # ajouterNom(listNom)
    afficherNom(listNom)
    possition(listNom)



main()