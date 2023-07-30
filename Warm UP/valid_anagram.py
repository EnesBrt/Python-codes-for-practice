# Fonction pour trouver si deux chaînes sont des anagrammes
def find_anagram(s, t):
    # Initialisation de deux dictionnaires pour compter les caractères dans 's' et 't'
    char_count_s = {}
    char_count_t = {}

    # Parcourir chaque caractère dans 's'
    for x in range(len(s)):
        # Si le caractère est déjà dans le dictionnaire, incrémenter le compte
        if s[x] in char_count_s:
            char_count_s[s[x]] += 1
        # Sinon, ajouter le caractère au dictionnaire avec un compte de 1
        else:
            char_count_s[s[x]] = 1

    # Faire la même chose pour 't'
    for y in range(len(t)):
        if t[y] in char_count_t:
            char_count_t[t[y]] += 1
        else:
            char_count_t[t[y]] = 1

    # Si les deux dictionnaires sont égaux, 's' et 't' sont des anagrammes, donc retourner True
    if char_count_s == char_count_t:
        return True
    # Sinon, 's' et 't' ne sont pas des anagrammes, donc retourner False
    else:
        return False



print(find_anagram("car","rac"))
