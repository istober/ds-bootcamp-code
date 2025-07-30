# Requerimiento 1
libro1 = {'titulo': 'Cien Años de Soledad', 'autor': 'Gabriel García Márquez', 'precio': 12000.0, 'stock': 5}
libro2 = {'titulo': '1984', 'autor': 'George Orwell', 'precio': 9000.0, 'stock': 3}
libro3 = {'titulo': 'El Principito', 'autor': 'Antoine de Saint-Exupéry', 'precio': 7000.0, 'stock': 10}
libro4 = {'titulo': 'Rayuela', 'autor': 'Julio Cortázar', 'precio': 11000.0, 'stock': 2}
libro5 = {'titulo': 'Fahrenheit 451', 'autor': 'Ray Bradbury', 'precio': 9500.0, 'stock': 1}

libros = [libro1, libro2, libro3, libro4, libro5]

# Requerimiento 6.1
descuentos_por_autor = {
    'Gabriel García Márquez': 0.10,
    'George Orwell': 0.05,
    'Julio Cortázar': 0.15
}

# Requerimiento 7
total_libros_comprados = 0
monto_total_pagado = 0.0
ahorro_total_descuentos = 0.0

# Requerimiento 2
def mostrar_libros_disponibles(libros):
    print("Lista de libros disponibles con más de 1 unidad en stock:")
    for libro in libros:
        if libro['stock'] > 1:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Stock: {libro['stock']}, Precio: ${libro['precio']}")

mostrar_libros_disponibles(libros)

# Requerimiento 3
min_precio = float(input("Ingrese el precio mínimo para filtrar los libros: "))
max_precio = float(input("Ingrese el precio máximo para filtrar los libros: "))

print(f"Libros con precio entre ${min_precio} y ${max_precio}:")
for libro in libros:
    if libro["precio"] < min_precio:
        pass
    elif libro["precio"] > max_precio:
        pass
    else:
        print(f"{libro['titulo']} por {libro['autor']} (${libro['precio']})")

# Requerimiento 4, 6.2 y 7
def comprar_libros(titulo, cantidad):
    global total_libros_comprados, monto_total_pagado, ahorro_total_descuentos

    libro_encontrado = None
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            libro_encontrado = libro
            break

    if libro_encontrado:
        if libro_encontrado['stock'] >= cantidad:
            libro['stock'] -= cantidad

            precio_total_sin_descuento = libro_encontrado['precio'] * cantidad
            descuento_aplicado_actual = 0

            autor = libro_encontrado['autor']
            if autor in descuentos_por_autor:
                porcentaje_descuento = descuentos_por_autor[autor]
                descuento_aplicado_actual = precio_total_sin_descuento * porcentaje_descuento
                precio_final_con_descuento = precio_total_sin_descuento - descuento_aplicado_actual
                
                print(f"¡Descuento del {int(porcentaje_descuento*100)}% aplicado por ser de {autor}!")
                print(f"Precio original: ${precio_total_sin_descuento}, Descuento: ${descuento_aplicado_actual}")
                print(f"Precio final con descuento: ${precio_final_con_descuento}.")
            else:
                precio_final_con_descuento = precio_total_sin_descuento
                print(f"Compra exitosa: {cantidad} copia(s) de '{libro_encontrado['titulo']}' por ${precio_final_con_descuento}.")

            total_libros_comprados += cantidad
            monto_total_pagado += precio_final_con_descuento
            ahorro_total_descuentos += descuento_aplicado_actual

        else:
            print(f"Lo sentimos, no hay suficiente stock para '{libro['titulo']}'. Stock disponible: {libro['stock']}.")
    else:
        print(f"Lo sentimos, el libro '{titulo}' no se encuentra en nuestro inventario.")

titulo = input("Ingrese el título del libro que desea comprar: ")
cantidad = int(input("Ingrese la cantidad de copias que desea comprar: "))
comprar_libros(titulo, cantidad)

# Requerimiento 5 y 7
while True:
    print("Menú de Compras")
    print("1. Mostrar libros disponibles")
    print("2. Filtrar libros por rango de precios")
    print("3. Comprar libros")
    print("4. Finalizar compra y mostrar factura")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        mostrar_libros_disponibles(libros)
    elif opcion == '2':
        min_precio = float(input("Ingrese el precio mínimo para filtrar los libros: "))
        max_precio = float(input("Ingrese el precio máximo para filtrar los libros: "))

        print(f"Libros con precio entre ${min_precio} y ${max_precio}:")
        for libro in libros:
            if libro["precio"] < min_precio:
                pass
            elif libro["precio"] > max_precio:
                pass
            else:
                print(f"{libro['titulo']} por {libro['autor']} (${libro['precio']})")
    elif opcion == '3':
        titulo = input("Ingrese el título del libro que desea comprar: ")
        cantidad = int(input("Ingrese la cantidad de copias que desea comprar: "))
        
        comprar_libros(titulo, cantidad)
    elif opcion == '4':
        print("Factura de Compra")
        print(f"Total de libros comprados: {total_libros_comprados}")
        print(f"Monto total pagado: ${monto_total_pagado}")
        print(f"Ahorro total por descuentos: ${ahorro_total_descuentos}")
        print("¡Hasta pronto!")
        break 
    else:
        print("Opción no válida. Por favor, intente de nuevo.")