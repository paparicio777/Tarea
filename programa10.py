#Pedro Aparicio Herrera - 250243
#tipo de cambio

# Solicitar al usuario la cantidad en pesos
pesos = float(input("Ingrese la cantidad en pesos: "))

# Solicitar el tipo de cambio (cuántos pesos equivale 1 dólar)
tipo_cambio = float(input("Ingrese el tipo de cambio (pesos por dólar): "))

# Calcular equivalencia en dólares
dolares = pesos / tipo_cambio

# Mostrar el resultado
print("Equivalente en dólares: $", round(dolares, 2))