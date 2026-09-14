# Punto 2
# Se tiene una cadena de texto ingresada por el usuario. Desarrolle un programa que recorra la cadena como iterable
# y determine la cantidad total de caracteres, la cantidad de vocales (a, e, i, o, u) y la cantidad de consonantes.

cadena = input("Ingrese una cadena: ")

while not cadena.replace(" ", "").isalpha():
    print("No se permiten números.")
    cadena = input("Ingrese una cadena: ")

caracteres = 0
vocales = 0
consonantes = 0

for caracter in cadena.lower():
    caracteres = caracteres + 1

    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        vocales = vocales + 1
    elif caracter != " ":
        consonantes = consonantes + 1

print("Cantidad de caracteres:", caracteres)
print("Cantidad de vocales:", vocales)
print("Cantidad de consonantes:", consonantes)
