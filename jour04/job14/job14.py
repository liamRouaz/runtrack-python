def my_long_word(longueur_minimale, chaine):
    mots = chaine.split()  # Divise la chaîne en une liste de mots
    mots_plus_longs = [mot for mot in mots if len(mot) > longueur_minimale]
    return mots_plus_longs

# Exemple d'utilisation de la fonction
longueur_minimale = 3
phrase = "Le python est un langage de programmation puissant et polyvalent."

resultat = my_long_word(longueur_minimale, phrase)

print(f"Mots de plus de {longueur_minimale} caractères :", resultat)
