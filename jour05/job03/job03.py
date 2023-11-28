def triangle(height):
    for i in range(height):
        spaces = " " * (height - i - 1)
        slashes = "/" * (2 * i + 1)
        print(spaces + slashes)

height = int(input("Entrez la hauteur du triangle : "))
triangle(height)
