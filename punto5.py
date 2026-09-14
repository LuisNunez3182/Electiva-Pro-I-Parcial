# Punto 5
# Se desea registrar productos y sus precios utilizando un diccionario.
# El programa debe permitir ingresar al menos 3 productos con su respectivo precio. Luego, debe recorrer el diccionario
# y mostrar todos los productos con sus precios, el producto más costoso y el precio promedio de los productos.

Productos = {}
 
CantidadProductos = int(input("¿Cuántos productos desea registrar? (minimo 3): "))
 
for i in range(CantidadProductos):
    Nombre = input(f"\nIngrese el nombre del producto {i + 1}: ")
    Precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    Productos[Nombre] = Precio
 
print("\nProductos registrados:")
for Nombre, Precio in Productos.items():
    print(f"{Nombre}: {Precio}")
 
ProductoMasCostoso = max(Productos, key=Productos.get)
print(f"\nEl producto mas costoso es: {ProductoMasCostoso} con un precio de {Productos[ProductoMasCostoso]}")
 
PrecioPromedio = sum(Productos.values()) / len(Productos)
print(f"El precio promedio de los productos es: {PrecioPromedio}")