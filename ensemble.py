#Les emsembles n'accepte pas d'element en double
#creation
# E = {1,2,3,4}
# E = set ((1,2,3,4))
# E = set(rang(0,10,2))
# E = frozenset((1,2,"En"))

#ajout
# E.add(element)
# E.update([1,"En","pop"]) - E.update({1,"En","pop"})

#supprimer
#E.remove(element) sinon erreur
#E.disccard(element) sans erreur
#E.pop() suprimer un element aleatoir
#E.clear() vider l'ensemble

#Methodes et fonctions
#len(E) nombre d'element
#sum(E)
#max(E)
#min(E)

#duplication
# E = Eorigine.copy()

#Operation
#  UNION
#E = E1 | E2 | ...; E1 | = E2 ou E =  E1.uinion(E2,E3,..); E1.update(E2)
# INTERSECTION
#E = E1 & E2 & E3...; E1 & = E2 ou E = E.intersection(E2,E3..); E1.intersection_update(E2)
# DIFFERENCE
#E = E1 - E2 ou E = E1.difference(E2) ; E1 -= E2 ; E1.difference_update(E2)
# DIFFERENCE SYMETRIQUE
#E1 ^= E2 ; E1.symmetric_difference_update(E2)
# SOUS ENSEMBLE
#B.issubset(A) => True ou False; B <= A
# SOUS ENSEMBLE PROPRE
# B < A
# SUR ENSEMBLE
# A.issuperset(B); A>=B
# SUR ENSEMBLE PROPRE
# A > B
#EGALITE
#A == B
# DISJOCTION
# A.isdisjoint(B)