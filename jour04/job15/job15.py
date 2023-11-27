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
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres dans la liste
ma_liste_arrondie = [round(nombre) for nombre in ma_liste]

# Afficher la liste avant le tri
print("Liste avant le tri :", ma_liste_arrondie)

# Appeler la fonction de tri
tri_bulles(ma_liste_arrondie)

# Afficher la liste après le tri
print("Liste après le tri :", ma_liste_arrondie)
