def afficher_tables_multiplication(N):
    if N <= 0:
        print("Veuillez saisir un entier supérieur à zéro.")
        return

    i = 1
    while i <= N:
        print(f"\nTable de multiplication de {i} :")
        j = 1
        while j <= 10:
            produit = i * j
            print(f"{i} x {j} = {produit}")
            j += 1
        i += 1

if __name__ == "__main__":
    try:
        N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))
        afficher_tables_multiplication(N)
    except ValueError:
        print("Veuillez saisir un entier valide.")
