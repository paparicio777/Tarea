#Pedro Aparicio Herrera - 250243
#Ganancia sobre la venta del producto

# Solicitar el precio de compra al usuario
precio_compra = float(input("Ingrese el precio de compra del artículo: "))

# Calcular la ganancia (30%)
ganancia = precio_compra * 0.30

# Calcular el precio de venta
precio_venta = precio_compra + ganancia

# Mostrar el resultado
print("El precio de venta para obtener una ganancia del 30% es: $", round(precio_venta, 2))