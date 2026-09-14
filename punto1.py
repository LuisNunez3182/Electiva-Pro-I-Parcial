# Punto 1
# Se tiene una lista de números enteros ingresados por el usuario. Desarrolle un programa que permita almacenar
# estos valores en una lista y luego muestre la suma total de los elementos, el número mayor y el número menor.

lista = []
n = int(input("¿Cuántos números desea ingresar? "))

for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    lista.append(numero)

suma_total = sum(lista)
mayor = max(lista)
menor = min(lista)

print("\nLista ingresada:", lista)
print("Suma total:", suma_total)
print("Número mayor:", mayor)
print("Número menor:", menor)
