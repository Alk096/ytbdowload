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
    for item in range(len(l)) : Parcourir les index de la liste
    for index, item in enumerate(l) : Parcourir les items avec leurs index
    for item, next_item in zip(l, l[1:]) : Parcourir les items et leurs suivants
    for a, b, c in zip(l1, l2, l3) : Parcourir plusieurs listes en parallèle
    for item in l if condition : Parcourir les items qui satisfont une condition
"""


#for item in range(len(list)):
    #    print(list[item])
#for index, item in enumerate(list):
#    print(f'Index : {index}, Item : {item}')
#for langues, noms, agees in zip(langues, noms, agees):
#    print(f'Langue : {langues}, Nom : {noms}, Age : {agees}')
