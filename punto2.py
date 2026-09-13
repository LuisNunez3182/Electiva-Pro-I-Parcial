cadena = input("Ingrese una cadena: ")

caracteres = 0
vocales = 0
consonantes = 0

for caracter in cadena:
    caracteres = caracteres + 1

    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        vocales = vocales + 1
    elif caracter != " ":
        consonantes = consonantes + 1

print("Cantidad de caracteres:", caracteres)
print("Cantidad de vocales:", vocales)
print("Cantidad de consonantes:", consonantes)
