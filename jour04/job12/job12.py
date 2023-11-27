def tri_bulles(liste):
    n = 0
    for _ in liste:
        n += 1

    # Effectuer un nombre d'itérations égal à la taille de la liste
    for i in range(n):
        # Parcourir la liste de la première à l'avant-dernière position
        for j in range(0, n - i - 1):
            # Échanger les éléments si l'élément actuel est plus grand que le suivant
            if liste[j] > liste[j + 1]:
                # Échanger les éléments
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp

# Exemple d'utilisation avec une liste
ma_liste = [64, 34, 25, 12, 22, 11, 90]

# Afficher la liste avant le tri
print("Liste avant le tri :", ma_liste)

# Appeler la fonction de tri
tri_bulles(ma_liste)

# Afficher la liste après le tri
print("Liste après le tri :", ma_liste)
