#Se tiene una lista de números enteros. 
# Desarrolle un programa que genere una nueva lista donde cada elemento sea el cuadrado del valor original. 
# Luego, muestre la lista resultante.

#Lista de los numeros enteros
numeros = [4, 24, 64, 84, 59]

#Nueva lista
resultado = []

#Recorremos la lista para poder usar la operación y guardamos en la nueva lista
for num in numeros:
    
    cuadrado = num * num
    resultado.append(cuadrado)
    
#Mostramos ambas listas: la original y la resultante
print("Lista original: ", numeros)
print("Lista resultante: ", resultado)
