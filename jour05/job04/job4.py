def tapis_diagonale(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print("X", end=" ")
            else:
                print("-", end=" ")
        print()

# Exemple d'utilisation avec une taille de 5
taille = 5
tapis_diagonale(taille)
