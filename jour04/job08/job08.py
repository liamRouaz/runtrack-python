L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialiser la variable somme à zéro
somme_des_valeurs_paires = 0

# Parcourir la liste et ajouter les valeurs paires à la somme
for nombre in L:
    if nombre % 2 == 0:
        somme_des_valeurs_paires += nombre

print("La somme des valeurs paires dans la liste est :", somme_des_valeurs_paires)
