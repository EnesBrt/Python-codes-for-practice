# Fonction pour trouver le premier caractère unique dans une chaîne


def first_unique_charatcter(string):

    # Initialisation de deux dictionnaires pour stocker les indices des caractères
    indices_non_unique_char = {}  # Pour les caractères qui apparaissent plus d'une fois
    indices_unique_chars = {}  # Pour les caractères qui apparaissent une seule fois

    # Parcourir chaque caractère dans la chaîne
    for x in range(len(string)):
        # Si le caractère est déjà dans indices_non_unique_char, ajouter l'indice à sa liste
        if string[x] in indices_non_unique_char:
            indices_non_unique_char[string[x]].append(x)
        else:
            # Si le caractère est déjà dans indices_unique_chars
            if string[x] in indices_unique_chars:
                # Le déplacer à indices_non_unique_char et ajouter l'indice à sa liste
                indices_non_unique_char[string[x]] = indices_unique_chars[string[x]]
                indices_non_unique_char[string[x]].append(x)
                # Et le supprimer de indices_unique_chars
                del indices_unique_chars[string[x]]
            else:
                # Si le caractère n'est pas encore dans indices_unique_chars, créer une nouvelle liste pour lui
                indices_unique_chars[string[x]] = [x]

    # Obtenir le premier caractère unique (la clé du premier élément dans indices_unique_chars)
    first_key = next(iter(indices_unique_chars))
    # Obtenir l'indice du premier caractère unique
    first_value = indices_unique_chars[first_key]

    # Retourner l'indice du premier caractère unique
    return first_value


# Tester la fonction avec la chaîne "leetcode", le premier caractère unique est 'l' à l'indice 0
print(first_unique_charatcter("leetcode"))
