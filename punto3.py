# Punto 3
# Se tiene una lista de palabras ingresadas por el usuario. Desarrolle un programa que recorra la lista y cree una nueva
# lista que contenga únicamente las palabras cuya longitud sea mayor a 5 caracteres. Al final, muestre la nueva lista.

texto_ingresado = input("Ingresa varias palabras separadas por espacios: ")
lista_palabras = texto_ingresado.split()
palabras_largas = []

for palabra in lista_palabras:
    if len(palabra) > 5:
        palabras_largas.append(palabra)

print("\nLa nueva lista con palabras de más de 5 caracteres es:")
print(palabras_largas)
