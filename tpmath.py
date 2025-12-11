"""
TP : Complexité et algorithmes en Python avec graphiques
Objectifs :
- Implémenter des fonctions de recherche et de tri
- Mesurer les performances avec timeit
- Visualiser la croissance des temps avec matplotlib
"""

import random
import timeit
import matplotlib.pyplot as plt

# -------------------------------
# Fonctions à compléter par les étudiants
# -------------------------------

def recherche_lineaire(lst, x):
    """Retourne l'indice de x dans lst ou -1 si non trouvé (O(n))"""
    
    for i, val in enumerate(lst):
        if val == x:
            return i
    return -1


def recherche_dichotomique(lst, x):
    """Retourne l'indice de x dans lst triée ou -1 si non trouvé (O(log n))"""
    
    gauche = 0
    droite = len(lst) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if lst[milieu] == x:
            return milieu
        elif lst[milieu] < x:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return -1


def tri_selection(lst):
    """Trie lst en utilisant le tri par sélection (O(n^2))"""
    
    lst = lst[:] 
    n = len(lst)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


def tri_rapide(lst):
    """Trie lst en utilisant QuickSort (O(n log n) en moyenne)"""
    
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    gauche = [x for x in lst if x < pivot]
    milieu = [x for x in lst if x == pivot]
    droite = [x for x in lst if x > pivot]

    return tri_rapide(gauche) + milieu + tri_rapide(droite)


# -------------------------------
# Fonctions utilitaires
# -------------------------------

def generer_liste(n, max_val=10000):
    return [random.randint(0, max_val) for _ in range(n)]

def mesurer_temps(fonction, *args, repetitions=1000):
    return timeit.timeit(lambda: fonction(*args), number=repetitions)

# -------------------------------
# Comparaison et visualisation
# -------------------------------

def comparer_recherche(tailles):
    temps_lineaire = []
    temps_dichotomique = []

    for n in tailles:
        lst = generer_liste(n)
        lst_sorted = sorted(lst)
        x = lst[-1]

        t_lin = mesurer_temps(recherche_lineaire, lst, x, repetitions=100)
        t_dic = mesurer_temps(recherche_dichotomique, lst_sorted, x, repetitions=100)

        temps_lineaire.append(t_lin)
        temps_dichotomique.append(t_dic)

    plt.figure(figsize=(8,5))
    plt.plot(tailles, temps_lineaire, 'o-', label='Recherche Linéaire (O(n))')
    plt.plot(tailles, temps_dichotomique, 's-', label='Recherche Dichotomique (O(log n))')
    plt.xlabel('Taille de la liste')
    plt.ylabel('Temps (s)')
    plt.title('Comparaison Recherche Linéaire vs Dichotomique')
    plt.legend()
    plt.grid(True)
    plt.show()

def comparer_tri(tailles):
    temps_selection = []
    temps_rapide = []

    for n in tailles:
        lst = generer_liste(n)

        t_sel = mesurer_temps(tri_selection, lst, repetitions=10)
        t_quick = mesurer_temps(tri_rapide, lst, repetitions=10)

        temps_selection.append(t_sel)
        temps_rapide.append(t_quick)

    plt.figure(figsize=(8,5))
    plt.plot(tailles, temps_selection, 'o-', label='Tri par sélection (O(n²))')
    plt.plot(tailles, temps_rapide, 's-', label='Tri rapide (O(n log n))')
    plt.xlabel('Taille de la liste')
    plt.ylabel('Temps (s)')
    plt.title('Comparaison Tri par sélection vs Tri rapide')
    plt.legend()
    plt.grid(True)
    plt.show()

# -------------------------------
# Mini-tests facultatifs pour les étudiants
# -------------------------------
def tests():
    lst = [3, 1, 4, 2, 5]
    lst_sorted = sorted(lst)
    try:
        assert recherche_lineaire(lst, 4) == 2
        assert recherche_lineaire(lst, 10) == -1
        assert recherche_dichotomique(lst_sorted, 4) == 2
        assert recherche_dichotomique(lst_sorted, 10) == -1
        assert tri_selection(lst) == sorted(lst)
        assert tri_rapide(lst) == sorted(lst)
        print("Tous les mini-tests passent !")
    except AssertionError:
        print("Mini-tests échoués, vérifiez vos fonctions.")

# -------------------------------
# Exécution TP
# -------------------------------
if __name__ == "__main__":
    print("=== Vérification des fonctions avec mini-tests ===")
    tests()

    tailles_recherche = [100, 500, 1000, 2000, 5000]
    tailles_tri = [100, 200, 500, 1000, 2000]

    print("\n=== Graphiques : Comparaison Recherche ===")
    comparer_recherche(tailles_recherche)

    print("\n=== Graphiques : Comparaison Tri ===")
    comparer_tri(tailles_tri)

