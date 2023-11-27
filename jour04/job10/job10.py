L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le produit à 1
produit_des_valeurs_dans_intervalle = 1

# Parcourir la liste et multiplier les valeurs dans l'intervalle [25, 90]
for valeur in L:
    if 25 <= valeur <= 90:
        produit_des_valeurs_dans_intervalle *= valeur

print("Le produit des valeurs dans l'intervalle [25, 90] est :", produit_des_valeurs_dans_intervalle)
