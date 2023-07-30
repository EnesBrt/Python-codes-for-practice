def longest_substring(s):
    # 'start' est l'indice du début de la sous-chaîne actuelle
    start = 0

    # 'max_length' est la longueur de la plus longue sous-chaîne sans répétition que nous avons trouvée jusqu'à présent
    max_length = 0

    # 'used_chars' est un dictionnaire qui garde une trace des caractères que nous avons déjà vus et de leur dernier indice
    used_chars = {}

    # 'max_substring' est la sous-chaîne la plus longue sans répétition que nous avons trouvée jusqu'à présent
    max_substring = ""

    # On commence une boucle qui va parcourir chaque caractère de la chaîne 's'
    for i in range(len(s)):
        # On vérifie si le caractère actuel a déjà été vu (c'est-à-dire s'il est dans 'used_chars') et si son dernier indice est après 'start'
        if s[i] in used_chars and start <= used_chars[s[i]]:
            # Si le caractère actuel est une répétition, on commence une nouvelle sous-chaîne juste après la première occurrence du caractère répété
            start = used_chars[s[i]] + 1
        else:
            # Si le caractère actuel n'est pas une répétition, on vérifie si la longueur de la sous-chaîne actuelle est plus grande que 'max_length'
            if max_length < i - start + 1:
                # Si c'est le cas, on met à jour 'max_length' et 'max_substring'
                max_length = i - start + 1
                max_substring = s[start:i+1]

        # On met à jour 'used_chars' pour indiquer que le caractère actuel a été vu à l'indice 'i'
        used_chars[s[i]] = i

    # Après avoir parcouru tous les caractères de 's', on renvoie 'max_substring', qui est la plus longue sous-chaîne sans répétition
    
    return max_substring
    

print(longest_substring("pccedfgder"))
