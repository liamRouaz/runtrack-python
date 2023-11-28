def draw_rectangle(width, height):
    for i in range(height):
    #si i est egale a 0 ou -1 ces la premiere est derniere ligne qui sont prise en compte car ont commence a l'indice 0
        if i == 0 or i == height - 1:
            print("--" * height)
        else:
            print("|" + "    " + "|")
        
draw_rectangle(10, 3)