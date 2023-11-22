def calcule(num1,operator,num2):
#si l'operateur (la variable en str) est egale a + alors aditione les deux valeur numerique.
    if operator == "+":
        return num1 + num2
#et si
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
            return num1 / num2
    
#appel de la fonction:
addition = calcule(5, "+", 3)
multiplication = calcule(4, "*", 6)
soustraction = calcule(10, "-", 7)
division = calcule(10, "/" , 2)

# Affichage des résultats
print("Résultat de l'addition : ", addition)
print("Résultat de la multiplication : ", multiplication)
print("Résultat de la multiplication : ", soustraction)
print("Résultat de la multiplication : ", division)



