job7 = [8, 24, 48, 2, 16]

# Initialiser le compteur à zéro
nombre_de_multiples_de_3 = 0

# Parcourir la liste et compter les multiples de 3
for nombre in job7:
    if nombre % 3 == 0:
        nombre_de_multiples_de_3 += 1

print("Le nombre de multiples de 3 dans la liste est :", nombre_de_multiples_de_3)
