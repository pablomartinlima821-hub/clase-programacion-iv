#Lista de productos con sus respectivos precios y stock
productos = [
     {"nombre": "Laptop", "precio": 1200, "stock": 15},
     {"nombre": "Mouse", "precio": 25, "stock": 5},
     {"nombre": "Teclado", "precio": 75, "stock": 25},
     {"nombre": "Monitor", "precio": 300, "stock": 8}
]
# #busca productos con bajo stock (menos de 10 unidades) y los almacena en una lista
# productos_bajo_stock = []
# #recorremos todos los productos de la lista
# for producto in productos:
# #Mostramos el nombre y el precio de cada producto
#     print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}")
# #verificamos si el stock es menor a 10
#     if producto['stock'] < 10:
# #Agregamos el producto a la lista de productos con bajo stock
#          productos_bajo_stock.append(producto)
# #Mostramos el titulo de los prodcutos con bajo stock
# print("\nProductos con bajo stock:")
# #Mostramos la lista de productos con bajo stock
# print(productos_bajo_stock)

#def crea una funcion
def calcular_promedio_precio(lista):
#if comprueba la condicion, pregunta si la lista esta vacia, si es asi devuelve 0
    if not lista:
#return devuelve un resultado de la funcion, si esta vacia muestra 0
       return 0
#sum suma los valores, len los cuenta, cuantos hay, esta linea suma todos los precios de los productos y los divide por la cantidad de productos para obtener el promedio
    total_precio = sum(p['precio'] for p in lista)
    return total_precio / len(lista)
#ejecuta la funcion y guarda el promedio
precio_promedio = calcular_promedio_precio(productos)
print(f"\nEl precio promedio de los productos es: ${precio_promedio:.2f}")

import csv

productos_desde_csv = []

with open('datos.csv', mode='r', encoding='utf-8') as archivo_csv:
    lector_diccionario = csv.DictReader(archivo_csv)
    for fila in lector_diccionario:
        fila['id'] = int(fila['id'])
        fila['precio'] = float(fila['precio'])
        fila['stock'] = int(fila['stock'])

        productos_desde_csv.append(fila)


print("\nLista de productos desde el archivo CSV:")
print(productos_desde_csv)

for producto in productos_desde_csv:
    print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}, Stock: {producto['stock']}")
