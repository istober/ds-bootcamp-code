# Requerimiento 1
productos = ['leche', 'pan', 'queso', 'mantequilla', 'yogur']

#Requerimiento 2
productos.append('huevo')
productos.append('jamón')
productos_destacados = productos[0:3]

# Requerimiento 3
inventario = {
    'producto1': {'nombre': 'leche', 'cantidad': 10},
    'producto2': {'nombre': 'pan', 'cantidad': 5},
    'producto3': {'nombre': 'queso', 'cantidad': 8},
    'producto4': {'nombre': 'mantequilla', 'cantidad': 3},
    'producto5': {'nombre': 'yogur', 'cantidad': 12},
}

# Requerimiento 4
inventario['producto6'] = {'nombre': 'huevo', 'cantidad': 20}
stock_producto1 = inventario['producto1']['cantidad']
print(f"Cantidad de producto1 (leche): {stock_producto1}")

# Requerimiento 5
categorias = ('Panadería', 'Lacteos')
categorias[1]
print(categorias[1])

# Requerimiento 6
t_cat = 'Panadería', 'Lacteos'
a, b = t_cat

# Requerimiento 7
productos_unicos = set(productos)
print(f"Productos únicos: {productos_unicos}")

# Requerimiento 8
productos_mayusculas = [producto.upper() for producto in productos]