alphabet = "abcdefghijklmnopqrstuvwxyz"
n = 10

for i in range(1, n + 1):
#for pour une boucle definy
    ligne = alphabet[:i]
    espaces = " " * (n - i)
    print(espaces + ligne)
