texto_ingresado = input("Ingresa varias palabras separadas por espacios: ")

lista_palabras = texto_ingresado.split()

palabras_largas = []

for palabra in lista_palabras:
    
    if len(palabra) > 5:
        palabras_largas.append(palabra)

print("\nLa nueva lista con palabras de más de 5 caracteres es:")
print(palabras_largas)