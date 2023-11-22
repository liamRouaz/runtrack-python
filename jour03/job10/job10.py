def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre > 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")


#appels de la fonction
verifier_pair_impair(8)
verifier_pair_impair(4)
verifier_pair_impair(0)
verifier_pair_impair(-10)
