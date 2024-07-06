import globales
import os
import math


def valor_mas_alto():
    todos_las_ventas=globales.leer_archivo_json("Ventas.json")
    productos= ["Café Americano","Té Chai","Croissant","Jugo Naranja","Panini de Pavo y Queso","Pastel de Zanahoria","Espresso Doble","Ba;do de Frutas","Muffin","Ensalada","Chocolate Caliente","Tarta de Frambuesa","Sándwich de Huevo","Galletas de Avena","Frappé de Caramelo"]
    valores_ordenados=sorted(todos_las_ventas,key=lambda x:x["valor"],reverse=True)

    for venta in valores_ordenados[:1]:
        nombre_producto=""
        for producto in productos:
            if producto== venta["nombre"]:
                nombre_producto=producto

        print(f"El valor mas alto es {venta["valor"]} de {nombre_producto}")

def valor_mas_bajo():
    todos_las_ventas=globales.leer_archivo_json("Ventas.json")
    productos= ["Café Americano","Té Chai","Croissant","Jugo Naranja","Panini de Pavo y Queso","Pastel de Zanahoria","Espresso Doble","Ba;do de Frutas","Muffin","Ensalada","Chocolate Caliente","Tarta de Frambuesa","Sándwich de Huevo","Galletas de Avena","Frappé de Caramelo"]
    valores_ordenados=sorted(todos_las_ventas,key=lambda x:x['iva'],reverse=False)

    for iva in valores_ordenados[:1]:
        nombre_productox=""
        for producto in productos:
            if producto == iva['nombre']:
                nombre_productox = producto
        print(f"El valor mas alto es {iva["iva"]} de {nombre_productox}")
        

def promedio_productos():
    todos_las_ventas=globales.leer_archivo_json("Ventas.json")
    suma_ventas=0
    cantidad_productos=0

    for venta in todos_las_ventas:
            suma_ventas+=venta["valor"]
            cantidad_productos+=1

            promedio_productos=suma_ventas/cantidad_productos
    print(f"El promedio de las ventas es ${int(promedio_productos)}")

def media_geometrica():
    todos_las_ventas=globales.leer_archivo_json("Ventas.json")
    suma_ventas=0
    cantidad_productos=0

    for venta in todos_las_ventas:
        suma_ventas=+ math.log(venta["valor"])
        cantidad_productos+=1

        media_geometrica=math.exp(suma_ventas/cantidad_productos)
    print(f"La media geometrica de las ventas es ${int(media_geometrica)}")
             
