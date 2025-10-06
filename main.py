#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # Initialisation
    C = [s[0]]  # liste des caractères rencontrés
    O = [1]     # liste du nombre d'occurrences correspondantes
    k = 1

    # Parcours de la chaîne
    while k < len(s):
        if s[k] == s[k - 1]:
            # même caractère → on augmente le compteur
            O[-1] += 1
        else:
            # nouveau caractère → on ajoute un nouvel élément
            C.append(s[k])
            O.append(1)
        k += 1

    # Fusion des deux listes en une liste de tuples
    return list(zip(C, O))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    
    if not s:
         return []

    # Compte le nombre de fois que le premier caractère se répète
    i = 1
    while i < len(s) and s[i] == s[0]:
        i += 1

    # Partie gauche : tuple du premier caractère et de son nombre d'occurrences
    gauche = [(s[0], i)]

    # Partie droite : appel récursif sur la chaîne restante
    droite = artcode_r(s[i:])

    return gauche + droite
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
