# Requerimiento 1
precio_producto = 1200
cantidad = 3
descuento = 10

# Requerimiento 2
total_sin_descuento = precio_producto * cantidad

# Requerimiento 3
monto_descuento = total_sin_descuento * (descuento / 100)

# Requerimiento 4
total_con_descuento = total_sin_descuento - monto_descuento

# Requerimiento 5
print("Total sin descuento: ",total_sin_descuento)
print("Monto de descuento: ",monto_descuento)
print("Total con descuento: ",total_con_descuento)