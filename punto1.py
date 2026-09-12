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
